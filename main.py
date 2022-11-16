from utils import *

from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "very secret secret key"

@app.route("/")
def index():
    return render_template("index.html",
                           get_flags = get_flags())

@app.route("/test")
def test():
    questions = [value for key, value in get_flags().items()]
    answers = [key for key, value in get_flags().items()]
    chosen_question = random.choice(questions)

    chosen_answers = [random.choice(answers) for _ in range(3)]
    chosen_answers.append(get_right_answer(get_flags(), chosen_question))

    task = {
        "question": chosen_question,
        "answers": chosen_answers,
        "right": get_right_answer(get_flags(), chosen_question)
    }
    # print(task)
    session["right_answer"] = task['right']

    return render_template("test.html",
                           task = task)


@app.route('/response')
def response():
    if 'right_answer' not in session:
        return 'Перейдите на главную'
    answer = request.args.get("answer")
    if answer == session["right_answer"]:
        return '<h1>Верно!</h1>'
    else:
        return '<h1>Неверно!</h1>'



app.run(host='0.0.0.0', port=81, debug=True)