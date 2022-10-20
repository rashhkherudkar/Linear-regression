from distutils.commad.config import config
from flask import Flask, jsonify, render_template, request
from Models.utils import medical_insurance_rashh_model
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcometo medical insurance")
    return render_template("index.html")


@app.route('/predict_charges', methods = ['POST', 'GET'])
def get_insurance_charges():

    if request.method == 'GET';
        print("We are using GET method")

        age = int(request.args.get('age'))
        sex = request.args.get('sex')
        bmi = float(request.args.get('bmi'))
        children = int(request.args.get('children'))
        smoker = request.args.get("smoker")
        region = request.args.get('region')
        