from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        return render_template("about.html")
    else:
        return render_template("about.html", form_data=request.form)


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return redirect("about")
    else:
        form_data = request.form
        return render_template("form.html", form_data=form_data)


if __name__ == "__main__":
    app.run(debug=True)
