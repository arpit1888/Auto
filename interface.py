from flask import Flask,jsonify,render_template,request
import config
from Project.utils import Auto

app = Flask(__name__)

@app.route("/")
def home_api():
    return render_template("index.html")

@app.route("/predict_price",methods=["GET","POST"])
def get_predicted_price():
    data = request.form
    symboling = int(data["symboling"])
    normalized_losses = int(data["normalized_losses"])
    make = data["make"]
    fuel_type = data["fuel_type"]
    aspiration = data["aspiration"]
    num_of_doors = data["num_of_doors"]
    body_style = data["body_style"]
    drive_wheels = data["drive_wheels"]
    engine_location = data["engine_location"]
    wheel_base = eval(data["wheel_base"])
    length = eval(data["length"])
    width = eval(data["width"])
    height = eval(data["height"])
    curb_weight = eval(data["curb_weight"])
    engine_type = data["engine_type"]
    num_of_cylinders = data["num_of_cylinders"]
    engine_size = eval(data["engine_size"])
    fuel_system = data["fuel_system"]
    bore = eval(data["bore"])
    stroke = eval(data["stroke"])
    compression_ratio = eval(data["compression_ratio"])
    horsepower = eval(data["horsepower"])
    peak_rpm = eval(data["peak_rpm"])
    city_mpg = eval(data["city_mpg"])
    highway_mpg = eval(data["highway_mpg"])
    car_price = Auto(symboling, normalized_losses, make, fuel_type, aspiration,
       num_of_doors, body_style, drive_wheels, engine_location,
       wheel_base, length, width, height, curb_weight, engine_type,
       num_of_cylinders, engine_size, fuel_system, bore, stroke,
       compression_ratio, horsepower, peak_rpm, city_mpg, highway_mpg)
    price = car_price.get_price()
    #return jsonify({"Result":f"Predicted Price: {price}"})
    return render_template ("index1.html",price=price)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER)
    