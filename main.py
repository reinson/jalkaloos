#!/usr/bin/env python
#
# Copyright 2007 Google Inc.

import random
from loosija import loosi_tiimid
import webapp2
import os
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape=True)


nimed = {"tormi": 1,
        "veiko":1,
        "fernando":1,
        "age":1,
        "rait":1,
        "eva":1,
        "sirle":1,
        "airiin":1,
        "matu":1,
        "margit":1,
        "vuss":1,
        "tanel":1,
        "kaur":1,
        "kaaren":1,
        "ardi":1,
        "tauri":1,
        "tom":1,
        "david":1,
        "tonis":1,
        "ular":1,
        "siim":1,
        "silver":1,
        
        }





class Handler(webapp2.RequestHandler):
    def write(self,*a,**kw):
        self.response.out.write(*a,**kw)

    def render_str(self, template,**params):
        t=jinja_env.get_template(template)
        return t.render(params)

    def render(self,template,**kw):
         self.write(self.render_str(template,**kw))


class MainHandler(Handler):
    def get(self):
        self.render("form.html",nimed = nimed)

    def post(self):
        kohal_olijad = []
        for nimi in nimed:
            kohal = self.request.get(nimi)
            if kohal:
                kohal_olijad.append(kohal)

        tiimid = loosi_tiimid(kohal_olijad,nimed)
        random.shuffle(tiimid[0])
        random.shuffle(tiimid[1])
        self.render("result.html", tiimid = tiimid)


class SuundHandler(Handler):
    def get(self):
        self.write(nimi)




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/suund",SuundHandler)
], debug=True)
