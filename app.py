# from flask import Flask

# app = Flask(__name__)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def items():
    return render_template('login.html')

# Other routes and configurations...

if __name__ == '__main__':
    app.run()