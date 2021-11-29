@app.route('/', methods=['GET','POST'])
def index():
    #get the make of the car 
    make = requests.get("")
    #get the shape
    shape = requests.get("")

    model_result = str(make.text) + " " + str(shape.text) 
   
   #post to service 4
    model = requests.post("", data=model_result)
    
    last_3_cars = car_generator.query.order_by(desc(car_generator.id)).limit(3).all()
    db.session.add(
      car_generator(
          make = make.text,
          shape = shape.text,
          model = model.text
      )
    )
    db.session.commit()
   
    return render_template('index.html', title='Car Generator', 
    make = make.text, 
    shape=shape.text, model = model.text, 
    pmodel_result=model_result, 
    last_3_car=last_3_cars)


