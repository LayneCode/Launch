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
import random


def getRandomFortune():
	fortunes = [
		"You will meet the person of your dreams",
		"I see a great field in front of you",
		"Carpe Diem",
		"Play that lucky number",
		"It is time for a great change",
		"It is best to know when to code, and when to super code",
		"All that glitters isn't glittery",
		"Eat more chikin"
	]
	rand_fort = fortunes[random.randint(0,len(fortunes)-1)]
	return rand_fort

class MainHandler(webapp2.RequestHandler):
    def get(self):
		header = "<h1>Fortune Cookie</h1>"
		
		
		
		fortune = "<strong>" + getRandomFortune() + "</strong>"
		fortune_sentence = "Your fortune: " + fortune
		fortune_pgraph = "<p>" + fortune_sentence + "</p>"
		
		lucky_num = "<strong>" + str(random.randint(1, 100)) + "</strong>"
		num_sentence = 'Your lucky number is: ' + lucky_num
		num_pgraph = "<p>" + num_sentence + "</p>"
		
		new = "Break open a new fortune cookie"
		new_a = '<a href=".">'+ new + '</a>'
		new_b = "<button>" + new_a + "</button>"
		
		content = header + fortune_pgraph + num_pgraph + new_b
		
		self.response.write(content)






app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
