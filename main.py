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


@app.route('/set', methods=['GET', 'POST'])
def set():
    # The function gets the set number from the form, finds the set from the lego.com website and returns the set.html
    if request.method == 'POST':
        set_num = request.form.get('set_num')
        try:
            set_object = brickable.find_set(set_num)
        except KeyError:
            error = 'Nincs találat'
            return render_template("set.html", error=error)

        else:
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
    top_results=[]
    # Cath error if no item was found
    try:
        Jofogas_AD = vatera_scrap.get_set_jofogas(set_num, set_name)
    except AttributeError:
        pass
    else:
        top_results.append(Jofogas_AD)



    Vatera_AD = vatera_scrap.get_set_vatera(set_num, set_name)

    top_results.append(Vatera_AD)


    try:
        Arukereso_AD = vatera_scrap.get_set_arukereso(set_num,set_name)
    except AttributeError:
        pass
    else:
        top_results.append(Arukereso_AD)


    try:
        Amazon_AD=vatera_scrap.get_set_amazon(set_num,set_name)

    except AttributeError:
        pass
    else:
        # If vatera_srcap found a AD but not the searched set it pass
        if Amazon_AD == None:
            pass
        else:
            top_results.append(Amazon_AD)

    Ebay_AD = ebay_api.get_set_ebay(set_num)
    top_results.append(Ebay_AD)

    top_results = sorted(top_results, key=lambda x: x.price)

    if top_results :


        return render_template("results.html", top_results=top_results)
    else:
        # If there is no result on the sites, show error on set.html
        error= "Sajnáljuk, a megadott LEGO egyik keresési oldalon sem található"
        return render_template("set.html", error=error)

@app.route('/results', methods=['GET', 'POST'])
def results():
    return render_template("results.html")
if __name__ == "__main__":
    app.run(debug=True)
