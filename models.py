from app import db
from app import ma
class ImageFlow(db.Model):
  uid = db.Column(db.Integer, primary_key=True) # the image id auto increment and the primary key
  url = db.Column(db.String(100))  # image url
  create_date = db.Column(db.DateTime)  #the date of insertion of the file at the first time
  lastmoddate = db.Column(db.DateTime) # after each step on the workflow the last modefication date will be changed so we can see when its the last time the image was on the workflow
  statusnumber = db.Column(db.String(1)) #the statusnumber will help us know at which state the image is in ! this will help us controll how to move between each step of the workflow
  statusmsg = db.Column(db.String(30)) # this for the status message and its changable

  def __init__(self, url , create_date,lastmoddate,statusnumber,statusmsg):
    self.url = url
    self.create_date = create_date
    self.lastmoddate = lastmoddate
    self.statusnumber = statusnumber
    self.statusmsg = statusmsg

class ProductSchema(ma.Schema):
  class Meta:
    fields = ('uid', 'url', 'create_date','lastmoddate','statusnumber','statusmsg')

img_schema = ProductSchema(strict=True)
imgs_schema = ProductSchema(many=True,strict=True)