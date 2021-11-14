from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return redirect("about")
    else:
        form_data = request.form
        return render_template("form.html", form_data=form_data)


if __name__ == "__main__":
    app.run(debug=True)
