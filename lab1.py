from flask import Flask, render_template

def calc():
   return 7

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'
app = Flask(__name__, static_url_path='/static')
@app.route('/')
def index():
    message = "lab1"
    return render_template('index.html', message=message)

@app.route('/lab1.html')
def lab1():
    test1 = calc()
    python_variable = "This is a Python variable for Lab 1!"
    return render_template('lab1.html', python_variable=python_variable, test1=test1)

if __name__ == '__main__':
    app.run(debug=True)
