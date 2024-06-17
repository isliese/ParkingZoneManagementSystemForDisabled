from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/Disabled')
def disabled():
    return render_template('Disabled.html')

@app.route('/Login')
def login():
    return render_template('Login.html')

@app.route('/LoginSuccess')
def loginsuccess():
    return render_template('LoginSuccess.html')

@app.route('/NoDisabled')
def nodisabled():
    return render_template('NoDisabled.html')

@app.route('/ParkingStateManaging')
def parkingstatemanaging():
    return render_template('ParkingStateManaging.html')

@app.route('/SignUp')
def signup():
    return render_template('SignUp.html')

@app.route('/SignUpSuccess')
def signupsuccess():
    return render_template('SignUpSuccess.html')

if __name__ == '__main__':
    app.run(debug=True)
