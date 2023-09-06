from flask import Flask,render_template,request
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])
def home():
    if request.method == "POST":

        number = request.form.get("phone")+request.form.get("mobile")
        num = phonenumbers.parse(number, "CH")
        country = geocoder.description_for_number(num,"en")

        num1 = phonenumbers.parse(number, "RO")
        sim = carrier.name_for_number(num1,"en")

        return render_template ("index.html", box = country, bag = sim )
    return render_template ("index.html")

if __name__ == "__main__":
    app.run(debug=True)