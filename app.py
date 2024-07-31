from flask import Flask, jsonify, request, render_template
from utils import get_data, add_task, delete_list_task

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        tasks = get_data("data.json")
        return render_template('main.html', tasks=tasks)
    if request.method == 'POST':
        delete_list_task()
        tasks = get_data("data.json")
        return render_template('main.html', tasks=tasks)


@app.route('/new/', methods=["GET", "POST"])
def new_task():
    if request.method == 'GET':
        return render_template('new_task.html')
    if request.method == 'POST':
        new_task = request.form["new_task"]
        add_task(new_task)
        return render_template("added.html")


@app.route('/delete/', methods=["GET", "POST"])
def delete_page():
    if request.method == 'GET':
        return render_template('delete_list.html')
    # if request.method == 'POST':
    #     new_task = request.form["new_task"]
    #     add_task(new_task)
    #     return render_template("added.html")


if __name__ == "__main__":
    app.run(debug=True)
