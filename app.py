from flask import Flask, render_template, request, flash
from val_api import get_top_rank

app = Flask(__name__)

@app.route("/")
def index():
    display_column_names, column_names, result = get_top_rank(10)
    return render_template("index.html", players = result, len=len(column_names), colnames=column_names, dispcolnames=display_column_names)

if __name__ == "__main__":
    app.run(debug=True)