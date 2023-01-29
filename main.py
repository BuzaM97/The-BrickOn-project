from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import brickable
import ebay_api
import vatera_scrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


# route that returns the "index.html" template.
@app.route('/')
def main():
    return render_template("index.html")


#  '/set' route and it handles both GET and POST requests.
@app.route('/set', methods=['GET', 'POST'])
def set():
    # The function gets the set number from the form, finds the set from the lego.com website and returns the set.html
    if request.method == 'POST':
        set_num = request.form.get('set_num')
        set_object = brickable.find_set(set_num)
        return render_template("set.html", set_num=set_num,
                               set_name=set_object.name,
                               set_year=set_object.year,
                               image=set_object.set_img_url)
    # If the request method is GET, it returns the "set.html" template
    return render_template("set.html")


@app.route('/search_jofogas', methods=['GET', 'POST'])
def search_jofogas():
    set_name = request.args.get('set_name')
    set_num = request.args.get('set_num')
    Jofogas_AD = vatera_scrap.get_set_jofogas(set_num, set_name)
    Vatera_AD = vatera_scrap.get_set_vatera(set_num, set_name)
    Arukereso_AD = vatera_scrap.get_set_arukereso(set_num,set_name)
    Amazon_AD=vatera_scrap.get_set_amazon(set_num,set_name)
    Ebay_AD = ebay_api.get_set_ebay(set_num)
    top_results = [
        Jofogas_AD,
        Vatera_AD,
        Arukereso_AD,
        Amazon_AD,
        Ebay_AD
    ]

    # Vatera_AD,
    # Arukereso_AD,
    # Amazon_AD,
    # Ebay_AD,
    return render_template("results.html", top_results=top_results)

@app.route('/results', methods=['GET', 'POST'])
def results():
    return render_template("results.html")
if __name__ == "__main__":
    app.run(debug=True)
