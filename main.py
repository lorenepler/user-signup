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
    if email=="":
        return True ##surely not best practice
    else:
        return EMAIL_RE.match(email)

header = "<h1>Signup</h1>"
username_label = "<label>Username</label>"
username = "<input type='text' name='username' value='%(username_value)s'><span style='color:red'> %(username_error)s</span>"
password_label = "<label>Password</label>"
password = "<input type='password' name='password'><span style='color:red'> %(password_error)s</span>"
verify_label = "<label>Verify Password</label>"
verify = "<input type='password' name ='verify'><span style='color:red'> %(verify_error)s</span>"
email_label = "<label>Email (optional)</label>"
email = "<input type='text' name='email' value='%(email_value)s'><span style='color:red'> %(email_error)s</span>"
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
                email_error="",
                username_value="",
                email_value=""): #when i switch parameters, error switches lines
        self.response.out.write(header + form % {"username_error":username_error,
                                                "password_error":password_error,
                                                "verify_error":verify_error,
                                                "email_error":email_error,
                                                "username_value":username_value,
                                                "email_value":email_value})

    def get(self):
        self.write_form()

    def post(self):
        username_input = self.request.get('username')
        password_input = self.request.get('password')
        verify_input = self.request.get('verify')
        email_input = self.request.get('email')

        valid_username = validate_username(username_input)
        valid_pass = validate_password(password_input)
        valid_verify = validate_verify(password_input,verify_input)
        valid_email = validate_email(email_input)

        params = dict(username_value=username_input, email_value=email_input)
        have_errors = False

        if not valid_username:
            params['username_error']="Invalid Username"
            have_errors=True
        if not valid_pass:
            params['password_error']="Invalid Password"
            have_errors=True
        if not valid_verify:
            params['verify_error']="Passwords do not match"
            have_errors=True
        if not valid_email:
            params['email_error']="Invalid Email"
            have_errors=True

        if have_errors==True:
            self.write_form(**params)
        else:
            self.response.out.write("<h1>Welcome, "+ username_input + "</h1>")

        #else:
        #    self.response.out.write("<h1>Welcome, "+ username + "</h1>")

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
