from flask import Flask, render_template, Response
import random 
from application import app

#get random make
@app.route('/make', methods=['GET'])
def make():
  makes = ["BMW", "Mercedes", "Audi", "VW"]
  make = random.choice(makes)
  return Response(make, mimetype="text/plain")