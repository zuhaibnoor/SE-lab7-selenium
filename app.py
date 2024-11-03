from flask import Flask, render_template, request
import time

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('template.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         return f"Form submitted: Name - {name}, Email - {email}"

if __name__ == '__main__':
    app.run(debug=True)
