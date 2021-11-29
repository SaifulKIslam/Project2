from flask import Flask, Response, request
import random
from application import app


@app.route('/model', methods=['GET', 'POST'])

def model(): 

        model_result = request.data.decode('utf-8')
        data = model_result.split(" ")
        shape = data[1]
        make = data[0]

        if make == "BMW":
                if shape == 'SUV':
                        model = 'X5'
                elif shape == 'Saloon':
                        model = '5 Series'
                elif shape == 'Hatchback':
                        model = '1 Series'
                elif shape == 'Coupe':
                        model = '4 Series'
        elif make == "Mercedes":
                if shape == 'SUV':
                        model = 'GLE'
                elif shape == 'Saloon':
                        model = 'E-Class'
                elif shape == 'Hatchback':
                        model = 'A-Class'
                elif shape == 'Coupe':
                        model = 'C-Class'
        elif make == "Audi":
                if shape == 'SUV':
                        model = 'Q7'
                elif shape == 'Saloon':
                        model = 'A6'
                elif shape == 'Hatchback':
                        model = 'A3'
                elif shape == 'Coupe':
                        model = 'A5'
        elif make == "VW":
                if shape == 'SUV':
                        model = 'Toureg'
                elif shape == 'Saloon':
                        model = 'Passat'
                elif shape == 'Hatchback':
                        model = 'Golf'
                elif shape == 'Coupe':
                        model = 'Arteon'
        
        return Response(model, mimeshape="text/plain")



