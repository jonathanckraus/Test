from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a=1
        b=2
        print(f"The sum is {add(a, b)}   -")
        if request.form.get('action1') == 'VALUE1':
            pass b
        elif  request.form.get('action2') == 'VALUE2':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html', form=form)
    print("Hello")
    return render_template("index.html")

