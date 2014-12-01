import os
import webapp2
import jinja2
from google.appengine.ext import db
from google.appengine.ext import blobstore
from google.appengine.api import images
from google.appengine.ext.webapp import blobstore_handlers
from urllib import quote
import sys
import traceback

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)
jinja_env.filters['fixurl'] = quote

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):   
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        self.render('home.htm')


    


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
