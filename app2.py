from flask import Flask, request, render_template, redirect, url_for
from tic_tac_toe import TicTacToe

tic_tac_toe = TicTacToe()
app2 = Flask(__name__)


def display():
    x = 1 if tic_tac_toe.is_relinquishing_starting_turn_possible() else 0
    return render_template('display1.html',
                           positions=tic_tac_toe.positions,
                           player=tic_tac_toe.players[0],
                           enable=x,
                           no_of_rows=tic_tac_toe.no_of_rows,
                           no_of_columns=tic_tac_toe.no_of_columns)


@app2.route("/rooms/roomid/reset", methods=['POST'])
def reset():
    tic_tac_toe.reset()
    return display()


@app2.route("/switch", methods=['POST'])
def switch():
    if tic_tac_toe.is_relinquishing_starting_turn_possible():
        tic_tac_toe.relinquish_starting_turn()
    else:
        pass
        # flash an error message
    return display()


@app2.route("/")
def index():
    return display()


@app2.route("/play", methods=['POST'])
def play():
    sub_value = request.form.get('sub')
    sub_value_int = int(sub_value)
    y1 = sub_value_int % 3
    x1 = sub_value_int // 3
    tic_tac_toe.play(x1, y1)
    winner = tic_tac_toe.get_winner()
    if winner is not None:
        return render_template('victory1.html',
                               positions=tic_tac_toe.positions,
                               player=winner,
                               no_of_rows=tic_tac_toe.no_of_rows,
                               no_of_columns=tic_tac_toe.no_of_columns)

    if tic_tac_toe.is_game_draw():
        return render_template('draw1.html',
                               positions=tic_tac_toe.positions,
                               no_of_rows=tic_tac_toe.no_of_rows,
                               no_of_columns=tic_tac_toe.no_of_columns)

    return redirect(url_for("index"))





















app2.run()
