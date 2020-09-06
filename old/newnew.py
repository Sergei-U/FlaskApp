from flask import Flask, render_template, request
import pandas as pd

def sortstr(Y):
    for i in range(1, len(Y)):
        b = Y[i]
        j = i - 1
        while (j >= 0) and (b < Y[j]):
            Y[j + 1] = Y[j]
            j -= 1
        Y[j + 1] = b
    return Y

app = Flask(__name__)
@app.route("/")
def first_page():
    return render_template("flask.html")
@app.route('/answer2', methods=['POST'])
def sortsting():
    string = list(map(int,request.form['string'].split()))
    string = sortstr(string)
    string = " ".join(map(str,string))
    return render_template('/flask.html', ans=string)


if __name__ == '__main__':
    app.run(debug=True)