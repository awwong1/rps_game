from flask import Blueprint, render_template
from rps_game.db import get_db

bp = Blueprint("score", __name__)

@bp.route("/score", methods=("GET",))
def show_score():
    """
    Logic for showing the score for a given player
    """

    db = get_db()
    scores = db.execute("""
      SELECT COUNT(*) as wins, playerA, playerB, playerWinner
      FROM rps_game
      WHERE playerWinner is not NULL
      AND playerAMove is not NULL
      AND playerBMove is not NULL
      GROUP BY playerA, playerB, playerWinner
      ORDER BY wins DESC
    """).fetchall()

    return render_template("score.html", scores=scores)
