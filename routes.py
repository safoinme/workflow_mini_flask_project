from flask import jsonify , request
from datetime import datetime as dt
from models import ImageFlow, imgs_schema, img_schema
from app import app ,db
# the root path shows all uploaded images
@app.route('/', methods=['GET'])
def get_images():
  all_images = ImageFlow.query.all()
  images = imgs_schema.dump(all_images)
  return jsonify(images.data)
#to insert an image only link is needed other informations are generated automaticly
@app.route('/imginsert', methods=['GET', 'POST'])
def insert_image():
  url = request.json['link']
  create_date=dt.now()
  lastmoddate=create_date
  statusnumber="0"
  statusmsg='image in initial state, just uploaded'
  new_image = ImageFlow(url, create_date,lastmoddate,statusnumber,statusmsg)

  db.session.add(new_image)
  db.session.commit()

  return img_schema.jsonify(new_image)
#by specifying the state1 path we can go to the first step and we can specify whatever message we want
@app.route('/state1', methods=['GET','POST'])
def go_state1():
  uid = request.json['uid']
  message = request.json['message']
  Image = ImageFlow.query.get(uid)
  Image.statusnumber=1  #status number is being changed automaticly at easy step
  Image.lastmoddate=dt.now()
  Image.statusmsg = message
  db.session.commit()
  return img_schema.jsonify(Image)

#by specifying the state2 path we can go to the second step and we can specify whatever message we want
@app.route('/state2', methods=['GET','POST'])
def go_state2():
  uid = request.json['uid']
  message = request.json['message']
  Image = ImageFlow.query.get(uid)
  Image.statusnumber=2
  Image.lastmoddate=dt.now()
  Image.statusmsg = message
  db.session.commit()
  return img_schema.jsonify(Image)

#by specifying the state3 path we can go to the final step and message is finished
@app.route('/state3', methods=['GET','POST'])
def go_state3():
  uid = request.json['uid']
  message = "finished"
  Image = ImageFlow.query.get(uid)
  Image.statusnumber=3
  Image.lastmoddate=dt.now()
  Image.statusmsg = message
  db.session.commit()
  return img_schema.jsonify(Image)