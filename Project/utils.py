import numpy as np
import pickle
import json
import config

class Auto():
    def __init__(self,symboling, normalized_losses, make, fuel_type, aspiration,
       num_of_doors, body_style, drive_wheels, engine_location,
       wheel_base, length, width, height, curb_weight, engine_type,
       num_of_cylinders, engine_size, fuel_system, bore, stroke,
       compression_ratio, horsepower, peak_rpm, city_mpg,
       highway_mpg):
       self.symboling = symboling
       self.normalized_losses = normalized_losses
       self.make = make
       self.fuel_type = fuel_type
       self.aspiration = aspiration
       self.num_of_doors = num_of_doors
       self.body_style ="body_style_" + body_style
       self.drive_wheels = "drive_wheels_" + drive_wheels
       self.engine_location = engine_location
       self.wheel_base = wheel_base
       self.length = length
       self.width = width
       self.height = height
       self.curb_weight = curb_weight
       self.engine_type = "engine_type_" + engine_type
       self.num_of_cylinders = num_of_cylinders
       self.engine_size = engine_size
       self.fuel_system = "fuel_system_" + fuel_system
       self.bore = bore
       self.stroke = stroke
       self.compression_ratio = compression_ratio
       self.horsepower = horsepower
       self.peak_rpm = peak_rpm
       self.city_mpg = city_mpg
       self.highway_mpg = highway_mpg

    def load_model(self):
        with open(config.MODEL_PKL,"rb") as f:
            self.model = pickle.load(f)
        with open(config.MODEL_JSON,"r") as f:
            self.json_data = json.load(f)
    
    def get_price(self):
        self.load_model()

        array = np.zeros(len(self.json_data["Columns"]))
        array[0] = self.symboling
        array[1] = self.normalized_losses
        array[2] = self.json_data["fuel_Type"][self.fuel_type]
        array[3] = self.json_data["aspiration_values"][self.aspiration]
        array[4] = self.json_data["num_of_doors_values"][self.num_of_doors]
        array[5] = self.json_data["engine_location_values"][self.engine_location]
        array[6] = self.wheel_base
        array[7] = self.length
        array[8] = self.width
        array[9] = self.height
        array[10] = self.curb_weight
        array[11] = self.json_data["num_of_Cylinders_values"][self.num_of_cylinders]
        array[12] = self.engine_size
        array[13] = self.bore
        array[14] = self.stroke
        array[15] = self.compression_ratio
        array[16] = self.horsepower
        array[17] = self.peak_rpm
        array[18] = self.city_mpg
        array[19] = self.highway_mpg
        

        make_index = self.json_data["Columns"].index(self.make)
        engine_type_index = self.json_data["Columns"].index(self.engine_type)
        fuel_system_index = self.json_data["Columns"].index(self.fuel_system)
        body_style_index = self.json_data["Columns"].index(self.body_style)
        drive_wheels_index = self.json_data["Columns"].index(self.drive_wheels)
        array[make_index] = 1
        array[engine_type_index] = 1
        array[fuel_system_index] = 1
        array[body_style_index] = 1
        array[drive_wheels_index] = 1

        print("array:",array)

        predicted_price = np.around(self.model.predict([array]),2)[0]
        return predicted_price


