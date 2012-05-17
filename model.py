from google.appengine.ext import db
from google.appengine.ext import blobstore

class Feedback(db.Model):
  name         = db.StringProperty()
  email        = db.StringProperty()
  phone_no     = db.StringProperty(default=None)
  comment      = db.StringProperty(multiline=True)
  date_joined  = db.DateTimeProperty(required=True)

