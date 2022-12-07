import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from rps_game.db import get_db

bp = Blueprint('game', __name__)

"""
Logic to show the new game form and handle new game creation.
"""
@bp.route('/', methods=('GET', 'POST'))
def new_game():
    if request.method == 'POST':
        # create a new game from the player names
        playerA = request.form.get('playerA', '').strip()
        playerB = request.form.get('playerB', '').strip()
        playerBComputer = request.form.get('playerBComputer', '').strip()

        error = None

        # very basic sanity checking
        if (playerA == playerB):
            error = 'Player names may not be the same.'
        elif (playerA == '🖥️' or playerB == '🖥️'):
            error = 'Player names may not be 🖥️'

        if (playerBComputer):
            playerB = None

        if error is None:
            db = get_db()
            try:
                db.execute(
                    "INSERT INTO rps_game (playerA, playerB) VALUES (?,?)",
                    (playerA, playerB)
                )
                db.commit()
            except Exception as err:
                error = err
            else:
                # redirect to the game page
                pass
                # return redirect(url_for('game.play'))
        flash(error)
    return render_template('new_game.html')

