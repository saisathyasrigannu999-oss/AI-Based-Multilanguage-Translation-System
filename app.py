from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""

    if request.method == "POST":
        text = request.form["text"]
        source = request.form["source"]
        target = request.form["target"]

        translated_text = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

    return render_template(
        "index.html",
        languages=languages,
        translated_text=translated_text
    )

if __name__ == "__main__":
    app.run(debug=True)