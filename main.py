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
import webapp2
import re

##def valid_username(username):
##    if username:
##        if username == "Loren":
##            return username

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def validate_username(username):
    return USER_RE.match(username)
def validate_password(password):
    return PASSWORD_RE.match(password)
def validate_verify(password, verify):
    if password == verify:
        return verify
def validate_email(email):
    return EMAIL_RE.match(email)


header = "<h1>Signup</h1>"
username_label = "<label>Username</label>"
username = "<input type='text' name='username'><span style='color:red'> %(username_error)s</span>"
password_label = "<label>Password</label>"
password = "<input type='password' name='password'><span style='color:red'> %(password_error)s</span>"
verify_label = "<label>Verify Password</label>"
verify = "<input type='password' name ='verify'><span style='color:red'> %(verify_error)s</span>"
email_label = "<label>Email (optional)</label>"
email = "<input type='text' name='email'><span style='color:red'> %(email_error)s</span>"
submit = "<input type='submit'>"

form = ("<form action='/' method='post'>" +
        username_label + username + "<br>" +
        password_label + password + "<br>" +
        verify_label + verify + "<br>" +
        email_label + email + "<br>" +
        submit +
        "</form>") ##action='/welcome' method='post'>" +

class MainHandler(webapp2.RequestHandler):
    def write_form(self,
                username_error="",
                password_error="",
                verify_error="",
                email_error=""): #when i switch parameters, error switches lines
        self.response.out.write(header + form % {"username_error":username_error,
                                                "password_error":password_error,
                                                "verify_error":verify_error,
                                                "email_error":email_error})

    def get(self):
        self.write_form()

    def post(self):
        valid_username = validate_username(self.request.get('username'))
        valid_pass = validate_password(self.request.get('password'))
        valid_verify = validate_verify(self.request.get('password'),self.request.get('verify'))
        valid_email = validate_email(self.request.get('email'))

        if not valid_username:
            self.write_form(username_error="Invalid Username")
        elif not valid_pass:
            self.write_form(password_error="Invalid Password")
        elif not valid_verify:
            self.write_form(verify_error="Passwords do not match")
        elif not valid_email:
            self.write_form(email_error="Invalid Email")
        else:
            self.response.out.write("Welcome!")

##class WelcomeHandler(webapp2.RequestHandler):
##
##    def post(self):
##        username = self.request.get("username")
##        content = "<h1>Welcome, "+ username + "!</h1>"
##        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
##    ('/welcome', WelcomeHandler)
], debug=True)
