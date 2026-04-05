from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return "this is login page"


if __name__=='__main__':
    app.run(debug=True)