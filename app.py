from flask import Flask, render_template, request
from utils import utils

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    all_risks = utils.get_all_risks()
    all_data = utils.load_csv()
    database_name = []
    fournisseurs = []
    if request.method == "POST":
        query = request.form.getlist("test_checkbox")
        corresponding_rows = utils.search(all_data, query)
        for row in corresponding_rows:
            fournisseurs += [{"nom du fournisseur" : all_data[row]["Nom du fournisseur"], "nom de la base": all_data[row]["Nom de la base"]}]
        return render_template("index.html", all_risks=all_risks, data = fournisseurs)
    return render_template("index.html", all_risks=all_risks)
