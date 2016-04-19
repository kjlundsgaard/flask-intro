from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<h1>Hi! This is the home page.</h1><a href=\"/hello\">Go to hello page</a>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name?</label> <input type="text" name="person">
          <label>Chose your greeting</label>
          <input type="radio" name="compliment" value="awesome"><label>Awesome</label>
          <input type="radio" name="compliment" value="terrific"><label>Terrific</label>
          <input type="radio" name="compliment" value="fantastic"><label>Fantastic</label>
          <input type="radio" name="compliment" value="neato"><label>Neato</label>
          <input type="radio" name="compliment" value="fantabulous"><label>Fantabulous</label>
          <input type="radio" name="compliment" value="wowza"><label>Wowza</label>
          <input type="radio" name="compliment" value="oh-so-not-meh"><label>Oh-so-not-meh</label>
          <input type="radio" name="compliment" value="brilliant"><label>Brilliant</label>
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")  
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
