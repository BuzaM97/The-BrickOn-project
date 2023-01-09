from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
import brickable
import set_class
import jinja2
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

Bootstrap(app)



@app.route('/')
def main():
    return render_template("index.html")

@app.route('/set', methods = ['GET', 'POST'])
def set():
    if request.method == 'POST':
        set_num = request.form.get('set_num')
        print(set_num)
        brickable.find_set(set_num)
        return render_template("set.html", set=brickable.find_set(set_num))

    return render_template("set.html")

if __name__ =="__main__":
    app.run(debug=True)
