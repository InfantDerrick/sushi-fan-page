from flask import *
from random import randrange

app = Flask(__name__)

questions = [['When is sushi\'s birthday?', 'December 18, 2020', 'January 15, 2021', 'June 14, 2021', '0'], ['What is sushi\'s breed?', 'Maine Coon', 'British Shorthair',
                                                                                                             'Orange Tabby', '1'], ['What is sushi\'s favorite toy?', 'Mooki', 'Wires', 'எலி', '2'], ['What is sushi\'s favorite food?', 'Friskies', 'Salmon', 'Chocolate', '3']]
fans = [['Angeline', 'Milton', '2021', '200'], ['Derrick', 'Gnanasusairaj', '2021', '200']]


@app.route("/", methods=["GET", "POST"])
def fanpage():
    if(request.method == "POST"):
        fans.append([request.form["FName"],request.form["LName"], request.form["membership"], request.form["points"]])
    return render_template("fanpage.html", fans = fans)


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == 'GET':
        return render_template('quiz.html', questions=questions[randrange(4)])
    selected = int(request.form['answer'])
    correct = 0
    formType = int(request.form['formType'])
    if (formType == 1):
        correct = 2
    elif (formType == 2):
        correct = 1

    if (correct == selected):
        return render_template('results.html', prompt="Well done, meow!")

    return render_template('results.html', prompt="Oh no :(")
