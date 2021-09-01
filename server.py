from flask import Flask, render_template

from functions.parse_todos import parse

app = Flask(__name__)

# @app.route('/')
# def show():
#     todo_file_name = "todo_list.json"
#     todos = parse(todo_file_name)
#     print(todos)
#     s = ""
#     for todo in todos['high']:
#         s += todo.context
#         s += "\n"
#     return s


@app.route('/show')
def show():
    todo_file_name = "todo_list.json"
    todos = parse(todo_file_name)

    return render_template('show.html', title='Home', todos=todos)

@app.route('/')
def index():
    return render_template('index.html')