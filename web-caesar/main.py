


import webapp2
import caesar

def BuildPage(textarea_content):


	rot_label = "<label>Rotate by:</label>"
	rotation_input = "<input type='number' name='rotation'/>"

	message_label = "<label>Input Message to Encrypt:</label>"

	text_area = "<textarea name='message''>" + textarea_content + "</textarea>"
	submit = "<input type='submit'/>"
	form = ("<form method='post'>" +
			message_label + text_area + "<br>" +
			rot_label + rotation_input + "<br>" +
			submit +
			"</form>")

	header = "<h2>Web Caesar</h2>"


	return header + form

class MainHandler(webapp2.RequestHandler):
	def get(self):

		content = BuildPage("")
		self.response.write(content)

	def post(self):

		message = self.request.get("message")
		rotation = int(self.request.get("rotation"))
		encrypted_message = caesar.encrypt(message, rotation)
		content = BuildPage(encrypted_message)
		self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
