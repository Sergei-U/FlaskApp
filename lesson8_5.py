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
def go():
    filename = 'programm.csv'
    with open(filename, 'w') as file_object:
        file_object.write('name')
        file_object.write(',')
        file_object.write('email')
        file_object.write(',')
        file_object.write('string1')
        file_object.write("\n")
    return render_template('1.html')

@app.route('/answer2', methods=['POST'])
def nn():
    filename = 'programm.csv'
    name = request.form['name']
    email = request.form['email']
    string = list(map(int,request.form['string1'].split()))
    string = sortstr(string)
    string = " ".join(map(str,string))
    with open(filename, 'a') as file_object:
        file_object.write(name)
        file_object.write(',')
        file_object.write(email)
        file_object.write(',')
        file_object.write(string)
        file_object.write("\n")

    return render_template('/1.html', ans=string)



@app.route("/")
def first_page():
    return render_template("flask.html")




# @app.route("/")
# def first_page():
#     return render_template("put.html")

@app.route("/")
def second_page():
    return render_template("put.html")

@app.route('/answer3', methods=['POST'])
def findsting():
    name1 = request.form['name1']
    f = pd.read_csv('programm.csv')
    answ2 = f[f['name'] == name1].values
    return render_template('put.html', ans2=answ2)


if __name__ == '__main__':
    app.run(debug=True)
