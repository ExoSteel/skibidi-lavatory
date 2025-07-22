from flask import Flask, redirect, url_for, request, render_template, make_response

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/youareanidiot")
def yaai():
    return render_template("yaai.html")

if __name__ == "__main__":
    app.run(port=5000)

