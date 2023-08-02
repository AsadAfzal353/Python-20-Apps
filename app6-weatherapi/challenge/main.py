from flask import Flask, render_template
import pandas as pd

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def api(word):
    df = pd.read_csv("app6-weatherapi/challenge/dictionary.csv")
    definition = df.loc[df["word"] == word]["definition"].squeeze()

    return {"definition": definition,
            "word": word}

if __name__ == "__main__":
    app.run(debug=True)