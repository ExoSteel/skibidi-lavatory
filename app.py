from flask import Flask, redirect, url_for, request, render_template, make_response

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/next", methods=['POST', 'GET'])
def next():
    if request.method == 'POST':
        email = request.form["email"]
        return render_template("next.html", email=email)
    else:
        return render_template("next.html", email="You aren't supposed to do that")

@app.route("/youareanidiot")
def yaai():
    return render_template("yaai.html")

if __name__ == "__main__":
    app.run(port=5000)

