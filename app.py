from flask import Flask, render_template, request, redirect

app=Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/merchants", methods=["GET", "POST"])
def merchants():
    if request.method=="POST":
        number=int(request.form("number"))
        mer_app=request.form("mer_app")
        txn_rate=int(request.form("txn_rate"))

        return redirect("/merchants")

    else:
        return render_template("merchants.html")

app.run(debug=True)