from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story
app = Flask(__name__)
app.config['SECRET_KEY'] = 'books_are_cool'
debug = DebugToolbarExtension(app)

# http://127.0.0.1:5000/madlibs
@app.route("/madlibs")
def ask_questions():
    """Generate and show form to ask words."""
    prompts = story.prompts
    return render_template("madlibs.html", prompts=prompts)

# http://127.0.0.1:5000/story
@app.route("/story")
def show_story():
    """Show story result."""
    text = story.generate(request.args)
    return render_template("story.html", text=text)