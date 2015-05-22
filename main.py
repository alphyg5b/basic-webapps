#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

###############################################################################################################################################
def escape_html(s):                                             ##                                   ##
        return cgi.escape(s, quote = True)                      ##  COMMON FUNCTION (HTML ESCAPING)  ##
                                                                ##                                   ##
###############################################################################################################################################

def cipher(var):                                                    
    tvar = ""                                                     
    varlen = len(var)                                                 
    for i in range(varlen):                                               ########################
        x = ord(var[i])                                                   ##                    ##
        if x>=97 and x<=122:                                              ##                    ##
            if x>=97 and x<=109:                                          ##     ROT 13         ##
                tvar+=chr(ord(var[i])+13)                                 ##                    ##
            else:                                                         ##    function        ##
                tvar+=chr(97+(ord(var[i])-110))                           ##                    ##
        elif x>=65 and x<=90:                                             ##                    ##
            if x>=65 and x<=77:                                           ########################  
                tvar+=chr(ord(var[i])+13)                                  
            else:                                                          
                tvar+=chr(65+(ord(var[i])-78))
        else:
                        tvar+=var[i]
    var = tvar
    return var

#################################################################################################################################################
import re
NAME_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_name(username):
    return NAME_RE.match(username)                                              #########################
                                                                                ##                     ##
PASS_RE = re.compile(r"^.{3,20}$")                                              ##     SIGN UP FORM    ##
def valid_pass(username):                                                       ##      VALIDATION     ##
    return PASS_RE.match(username)                                              ##                     ##
                                                                                ##                     ##
MAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")                                   #########################
def valid_mail(username):
    return MAIL_RE.match(username) or username == ''


#################################################################################################################################################
                                                                                                    ##        ROT 13     ##
                                                                                                    ##         HTML      ##
                                                                                                    #######################
rot13 = """<head><title>cipher text</title>
            </head><font color="red" face = "Kristen ITC" size = "+2"><h1>Enter some text to ROT13:<br>
            (preserves punctuation,white spaces and case)</h1></font>
            <br><font color="red" face = "Kristen ITC" size = "+2">
            <a href="https://en.wikipedia.org/wiki/ROT13">Here's some info about ROT13</a></font><br><br>
          <body
          background="http://funlava.com/wp-content/uploads/2013/03/cool-background-in-prince-of-persia_1024x768.jpg">
          <form method="post">
              <textarea name="text"
              style="height: 100px; width: 400px;" >%(string)s</textarea>
              <br>
              <a href="/signup"><font size = "+2">validation<sup>2<sup><font></a>
              <br><br><input type="submit" >
          </form></body>"""


####################################################################################################################################################
action = """<br><a href ="/test">ROT13<sup>1</sup></a>"""                          #    FRONT PAGE LINK   #

####################################################################################################################################################
                                                            ##                      ##
                                                            ##    SIGN UP HTML      ##
                                                            ##                      ##
                                                            ##########################
sign = """
  <html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right; color: green}
      .error {color: red}
      .green {color: green; font-size: 44}
    </style>

  </head>

  <body background="http://wallpup.com/wp-content/uploads/2013/03/Cool-Backgrounds-Wallpaper-HD.jpg">
    <h2 class="green">Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value=%(name)s>
          </td>
          <td class="error">
            %(nameerror)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="">
          </td>
          <td class="error">
            %(passerror)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="">
          </td>
          <td class="error">
            %(verifyerror)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value=%(mail)s>
          </td>
          <td class="error">
            %(emailerror)s
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>

</html>
        """
####################################################################################################################################################


import webapp2
import cgi

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/Html'
        self.response.write('Hello, Udacity!')
        self.response.write(action)
        
class TestHandler(webapp2.RequestHandler):
    def write_rot(self,string = ""):
        self.response.write(rot13 % {'string': string})

    def get(self):
        self.response.headers['Content-Type'] = 'text/Html'
        self.write_rot()

    def post(self):
        self.response.headers['Content-Type'] = 'text/Html'
        user_text = self.request.get('text')
        self.write_rot(escape_html(cipher(user_text)))

class Signup(webapp2.RequestHandler):
    def write(self,name="" , nameerror="" , passerror="" , verifyerror="" , mail="" , emailerror=""):
        self.response.write(sign % {'name' : name, 'nameerror': nameerror, 'passerror' : passerror, 'verifyerror' : verifyerror, 'mail': mail, 'emailerror': emailerror})

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.write()

    def post(self):
        self.response.headers['Content-Type'] = 'text/Html'
        user_name = self.request.get('username')
        user_pass = self.request.get('password')
        user_verify = self.request.get('verify')
        user_mail = self.request.get('email')
        if not valid_name(user_name) and not valid_pass(user_pass) and not valid_mail(user_mail):
            self.write(escape_html(user_name),"That's not a valid username.","That wasn't a valid password.","",escape_html(user_mail),"That's not a valid email.")
        elif valid_name(user_name) and not valid_pass(user_pass) and not valid_mail(user_mail):
            self.write(escape_html(user_name),"","That wasn't a valid password.","",escape_html(user_mail),"That's not a valid email.")
        elif not valid_name(user_name) and valid_pass(user_pass) and not valid_mail(user_mail):
            if user_pass == user_verify:
                self.write(user_name,"That's not a valid username.","","",user_mail,"That's not a valid email.")
            else:
                self.write(escape_html(user_name),"That's not a valid username.","","Your passwords didn't match.",escape_html(user_mail),"That's not a valid email.")
        elif not valid_name(user_name) and not valid_pass(user_pass) and valid_mail(user_mail):
            self.write(escape_html(user_name),"That's not a valid username.","That wasn't a valid password.","",escape_html(user_mail),"")
        elif valid_name(user_name) and not valid_pass(user_pass) and valid_mail(user_mail):
            self.write(escape_html(user_name),"","That wasn't a valid password.","",escape_html(user_mail),"")
        elif valid_name(user_name) and valid_pass(user_pass) and not valid_mail(user_mail):
            if user_pass == user_verify:
                self.write(escape_html(user_name),"","","",escape_html(user_mail),"That's not a valid email.")
            else:
                self.write(escape_html(user_name),"","","Your passwords didn't match.",escape_html(user_mail),"That's not a valid email.")
        elif not valid_name(user_name) and valid_pass(user_pass) and valid_mail(user_mail):
            if user_pass == user_verify:
                self.write(escape_html(user_name),"That's not a valid username.","","",escape_html(user_mail),"")
            else:
                self.write(escape_html(user_name),"That's not a valid username.","","Your passwords didn't match.",escape_html(user_mail),"")
        else:
            if user_pass != user_verify:
                self.write(escape_html(user_name),"","","Your passwords didn't match.",escape_html(user_mail),"")
            else:
                self.redirect("/welcome?name=" + user_name)

class Welcome(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/Html'
        self.response.write("<h2>Welcome, %s!</h2>" % self.request.get('name'))



    
app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/test', TestHandler),
                               ('/signup', Signup),
                               ('/welcome',Welcome)],
                              debug=True)
