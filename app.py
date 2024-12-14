from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app=Flask(__name__)

my_client=MongoClient("localhost", 27017)
my_paylater=my_client["paylater"]
my_merchant=my_paylater["merchant"]
my_order = my_paylater["order"]
my_payment = my_paylater["payment"]

@app.route("/orders", methods = ["GET"])
def orders():
    return render_template("orders.html")

@app.route("/payment", methods = ["GET"])
def payment():
    return render_template("payment.html")

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/merchants", methods=["GET", "POST"])
def merchants():
    if request.method=="POST":
        number=int(request.form("mer_id"))
        mer_app=request.form("mer_app")
        txn_rate=int(request.form("txn_rate"))
        my_merchant.insert_one({"number": number}, {"mer_app":mer_app}, {"txn_rate":txn_rate})
        return redirect("/merchants")

    else:
        return render_template("merchants.html")

app.run(debug=True)