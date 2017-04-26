import webapp2, cgi, os, re
import jinja2
from google.appengine.ext import db

# set up jinja
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))




class Index(Handler):
    def get(self):

        posts = db.GqlQuery("SELECT * FROM BlogPost ORDER BY created DESC LIMIT 5)

        t = jinja_env.get_template("frontpage.html")
        content = t.render(
                        posts = posts
                        )
        self.response.write(content)

class BlogPost(db.Model):
    """ Represents a movie that a user wants to watch or has watched """
    title = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)



class AddPost(Handler):
    #used for adding a new post

    def render_front(self, title="", content="", error1="", error2=""):
        self.render("add.html", title=title, content=content, error1=error1, error2=error2)

    def get(self):



        self.render_front()


    def post(self):

        title = self.request.get("title")
        content = self.request.get("content")
        error1 = ""
        error2 = ""


        if title and content:
            post = BlogPost(title=title, content=content)
            post.put()
            self.redirect('/blog/%s' % int(post.key().id()))

        if title == "" and content == "":
            error1 = "We need a title..."
            error2 = "We need content..."
            self.render_front(title, content, error1, error2)

        if title == "" and content != "":
            error1 = "We also need a title."
            self.render_front(title, content, error1, error2)

        if content == "" and title != "":
            error2 = "We also need some content."
            self.render_front(title, content, error1, error2)

class ViewPostHandler(Handler):
    def get(self, id):

        if BlogPost.get_by_id(int(id)):
            post = BlogPost.get_by_id(int(id))
            self.render("single-post.html", post=post)



app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddPost),
    webapp2.Route('/blog/<id:\d+>', ViewPostHandler),
], debug=True)
