from flask import Flask

app= Flask(__name__)

@app.route('/')
def hello_home():
    return '<p> You have reached home page </p> <img src"https://www.dictionary.com/e/wp-content/uploads/2018/04/Mojo-Jojo.jpg" />'

app.run(host="0.0.0.0", port=5000)
