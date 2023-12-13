from flask import Flask, render_template
import tkinter as tk
#import ImageTk
import random

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lab1.html')
def lab1():
  
    return render_template('lab1.html')

if __name__ == '__main__':
    app.run(debug=True)
