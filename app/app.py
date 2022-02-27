from collections import deque
import os

from flask import Flask, render_template, request, session

from elozza import elozza_response

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY', 'BBBBBBBBBB')

MAX_NUM_QUESTIONS = 5


# ====================
@app.route("/", methods=["GET", "POST"])
def talk_to_elozza():

    # Set up session variable to store dialogue history
    if "dialogue" not in session:
        session["dialogue"] = []

    if request.method == "POST":
        question = str(request.form["question"])
        if question:
            session["dialogue"].insert(0, {'question': question,
                                           'answer': elozza_response(question)})
            session["dialogue"] = session["dialogue"][0:MAX_NUM_QUESTIONS]
            session.modified = True

    return render_template('index.html', dialogue=list(session['dialogue']))


# ====================
if __name__ == "__main__":

    app.run(debug=True)
