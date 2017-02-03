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
def valid_username(username):
    return USER_RE.match(username)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Signup</h1>"
        username_label = "<label>Username</label>"
        username = "<input type='text' name='username'>"
        password_label = "<label>Password</label>"
        password = "<input type='password'>"
        verify_label = "<label>Verify Password</label>"
        verify = "<input type='password'>"
        email_label = "<label>Email (optional)</label>"
        email = "<input type='text'>"
        submit = "<input type='submit'>"

        form = ("<form action='/welcome' method='post'>" +
                username_label + username + "<br>" +
                password_label + password + "<br>" +
                verify_label + verify + "<br>" +
                email_label + email + "<br>" +
                submit +
                "</form>")
        self.response.write(header + form)

class WelcomeHandler(webapp2.RequestHandler):

    def post(self):
        username = self.request.get("username")
        content = "<h1>Welcome, "+ username + "!</h1>"
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
