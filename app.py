from flask import Flask, render_template

app = Flask(__name__)



#displays index page
@app.get('/')
def index():
    return render_template('index.html')


@app.get('/page2')
def second():
    return render_template('other.html')

@app.get('/page3')
def third():
    return render_template('p3.html')