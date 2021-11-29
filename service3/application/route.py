from flask import Flask, render_template, Response
import random 
from application import app

#get random shape
@app.route('/shape', methods=['GET'])
def shape():
  shapes = ["SUV", "Saloon", "Hatchback", "Coupe"]
  shape = random.choice(shapes)
  return Response(shape, mimeshape="text/plain")