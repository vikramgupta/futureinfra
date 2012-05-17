#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import urlfetch
from google.appengine.api import users
from google.appengine.api import memcache
from google.appengine.api import mail
import logging, sys, os, model
from datetime import datetime
import formats

class MainHandler(webapp.RequestHandler):
  def get(self):
    ip = self.request.remote_addr
    logging.info("user visited from ip: " + ip)

    template_values = {
        "page_header": formats.PageHeader("home"),
        "page_footer": formats.PageFooter(" ")
        }

    page = os.path.join(os.path.dirname(__file__), "templates", "index.html")
    self.response.out.write(template.render(page, template_values))

  def post(self):
    ip = self.request.remote_addr
    logging.info("post method called from ip: " + ip);
    self.response.out.write("<h3>Page under construction...</h3><br>Please visit the site after some time...")

class AboutUsHandler(webapp.RequestHandler):
  def get(self):
    template_values = {
        "page_header": formats.PageHeader("aboutus"),
        "page_footer": formats.PageFooter(" ")
        }

    page = os.path.join(os.path.dirname(__file__), "templates", "aboutus.html")
    self.response.out.write(template.render(page, template_values))

class ProfileHandler(webapp.RequestHandler):
  def get(self):
    template_values = {
        "page_header": formats.PageHeader("profile"),
        "page_footer": formats.PageFooter(" ")
        }

    page = os.path.join(os.path.dirname(__file__), "templates", "profile.html")
    self.response.out.write(template.render(page, template_values))

class ProjectsHandler(webapp.RequestHandler):
  def get(self):
    template_values = {
        "page_header": formats.PageHeader("projects"),
        "page_footer": formats.PageFooter(" ")
        }

    page = os.path.join(os.path.dirname(__file__), "templates", "projects.html")
    self.response.out.write(template.render(page, template_values))

class ServicesHandler(webapp.RequestHandler):
  def get(self):
    template_values = {
        "page_header": formats.PageHeader("services"),
        "page_footer": formats.PageFooter(" ")
        }

    page = os.path.join(os.path.dirname(__file__), "templates", "services.html")
    self.response.out.write(template.render(page, template_values))

class DealershipHandler(webapp.RequestHandler):
  def get(self):
    template_values = {
        "page_header": formats.PageHeader("dealers"),
        "page_footer": formats.PageFooter(" ")
        }

    page = os.path.join(os.path.dirname(__file__), "templates", "dealers.html")
    self.response.out.write(template.render(page, template_values))

class FeedbackHandler(webapp.RequestHandler):
  def get(self):
    logging.info("got post request FEEDBACK ................................................");

    name = self.request.get("name")
    email = self.request.get("email")
    phone = self.request.get("phone")
    comment = self.request.get("comment")

    db_entry = model.Feedback(
        name = name,
        email = email,
        phone = phone,
        comment = comment,
        date_joined = datetime.now()
        )
    db_entry.put()
    self.response.out.write("success")

    body_html = """
<html><head></head><body>
Hello,<br>
<br>
A feedback has been submitted. Here are the details:
  Name: %s
  Email: %s
  phone: %s
  comment: %s
</body></html>
    """ % (name, email, phone, comment)
    body_txt = body_html

    logging.info("message body = %s" % body_txt)

    message = mail.EmailMessage(sender="FutureInfra support<futureinframail@gmail.com>",
        subject="A new feedback has been posted")
    message.body = body_txt
    message.html = body_html
    message.to = "futureinframail@gmail.com"
    message.send()

    logging.info("sent mail..................................................................")

  def post(self):
    logging.info("got GET request FEEDBACK ................................................");

def main():
	application = webapp.WSGIApplication([
			('/',     		        		MainHandler),
			('/main',           			MainHandler),
			('/aboutus',          	  AboutUsHandler),
			('/profile',          	  ProfileHandler),
			('/projects',             ProjectsHandler),
			('/feedback',             FeedbackHandler),
			('/dealers',              DealershipHandler),
			('/services',             ServicesHandler)
			],
			debug=False)

	util.run_wsgi_app(application)

if __name__ == '__main__':
	main()
