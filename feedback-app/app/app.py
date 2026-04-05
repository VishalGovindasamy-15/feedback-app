from flask import Flask 

app=Flask(__name__)

@app.route('/')
def home():
    return "this is home page"

@app.route('/login')
def login():
    return "this is login page"


if __name__=='__main__':
    app.run(debug=True)