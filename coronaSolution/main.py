from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/lover')
def lovely():
    return app.send_static_file("x.html")


app.run(debug=True)
