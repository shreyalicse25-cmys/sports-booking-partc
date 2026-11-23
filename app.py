from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Sports Booking"

@app.route('/cricket')
def cricket():
    return "Cricket Booking"

@app.route('/football')
def football():
    return "Football Booking"

if __name__ == '__main__':
    app.run(debug=True)