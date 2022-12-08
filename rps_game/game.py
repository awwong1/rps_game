import functools
from random import choice
from datetime import datetime
from flask import (
    abort,
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

from rps_game.db import get_db

bp = Blueprint("game", __name__)
valid_moves = ("rock", "paper", "scissors")
win_map = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper',
}

def determine_winner(player_a_move, player_b_move):
    """
    Utility function to determine who won the game.
    Returns 'playerA', 'playerB' or None for tie/invalid.
    """
    if player_a_move not in valid_moves:
        return None
    if player_b_move not in valid_moves:
        return None
    if player_a_move == player_b_move:
        return None
    elif win_map[player_a_move] == player_b_move:
        return 'playerA'
    elif win_map[player_b_move] == player_a_move:
        return 'playerB'

def get_game(id):
    """
    Retrieve the Game SQL row from our database by ID
    """
    game = get_db().execute("SELECT * FROM rps_game WHERE id = ?", (id,)).fetchone()
    if game is None:
        abort(404, f"Game id {id} does not exist.")
    return game

@bp.route("/", methods=("GET", "POST"))
def new_game():
    """
    Logic to show the new game form and handle new game creation.
    """
    if request.method == "POST":
        # create a new game from the player names
        player_a = request.form.get("playerA", "").strip()
        player_b = request.form.get("playerB", "").strip()
        player_b_computer = request.form.get("playerBComputer", "").strip()

        error = None

        # very basic sanity checking
        if player_a == player_b:
            error = "Player names may not be the same."

        if player_b_computer:
            # computer value overrides name for player b
            player_b = None

        if error is None:
            db = get_db()
            cursor = db.cursor()
            try:
                cursor.execute(
                    "INSERT INTO rps_game (playerA, playerB) VALUES (?,?)",
                    (player_a, player_b),
                )
                db.commit()
            except Exception as err:
                error = err
            else:
                # redirect to the game page
                return redirect(url_for(".play_game", id=cursor.lastrowid))
        flash(error)
    return render_template("new_game.html")


@bp.route("/play/<int:id>", methods=("GET", "POST"))
def play_game(id):
    game = get_game(id)

    # extra visibility for client rendering
    messages = [f"Game created at {game['created']}"]

    if request.method == "POST":
        # update the game state
        error = None

        # what was the game move
        move = request.form.get("move", "").strip()
        if move not in valid_moves:
            error = f"Move must be one of {valid_moves}"

        # which player made the game move
        player_a_move = game["playerAMove"]
        player_b_move = game["playerBMove"]
        if player_a_move is None:
            player_a_move = move
            # if player B is a computer, make its move now
            if game["playerB"] is None:
                player_b_move = choice(valid_moves)
        elif player_b_move is None:
            player_b_move = move
        else:
            error = f"Invalid move, both players already went."

        # if both moves have been made, determine the winner
        player_winner = game["playerWinner"]
        if player_winner is None:
            winner = determine_winner(player_a_move, player_b_move)
            if winner == "playerA":
                player_winner = game["playerA"]
            elif winner == "playerB":
                player_winner = game["planerB"]

        if error is None:
            db = get_db()
            cursor = db.cursor()
            try:
                cursor.execute(
                    """
                    UPDATE rps_game
                    SET playerAMove = ?, playerBMove = ?, playerWinner = ?, modified = ?
                    WHERE id = ?
                    """,
                    (player_a_move, player_b_move, player_winner, datetime.now(), id),
                )
                db.commit()
                game = get_game(id)
            except Exception as err:
                error = err
        flash(error)

    # view render logic. Is it player_a or player_b's turn, or is the game over?
    game_state = None
    if game["playerAMove"] is None:
        game_state = f"{game['playerA']}: First Player's turn"
    elif game["playerBMove"] is None:
        game_state = f"{game['playerB']}: Second Player's turn"
    else:
        # both players have already moved
        game_state = "Finished"

    # helper messages for tracking moves
    if game["playerAMove"]:
        message_player_a = f"{game['playerA']} moved"
        if game_state == "Finished":
            message_player_a = f"{message_player_a} ({game['playerAMove']})"
        messages.append(message_player_a)
    if game["playerBMove"]:
        message_player_b = f"{game['playerB'] or '🖥️'} moved"
        if game_state == "Finished":
            message_player_b = f"{message_player_b} ({game['playerBMove']})"
        messages.append(message_player_b)
    if game_state == "Finished":
        if game['playerWinner']:
            message_winner = f"{game['playerWinner']} won the game!"
        else:
            message_winner = "No winner (tie)"
        messages.append(message_winner)
    messages.append(f"Game last modified at {game['modified']}")

    return render_template(
        "play_game.html", game_state=game_state, messages=messages, game=dict(game)
    )
