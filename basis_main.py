from flask import Flask

app = Flask (__name__)


@app.route ('/') # a decorator, wrap a function in its behavior in some type of way
# routing or mapping your function to the website. You need a return statement. When the user goes to the homepage, that is what they'll see##
def index():
    return 'This is the homepage'


@app.route('/tuna')
def tun():
    return '<h2>tuna is good</h2>'


@app.route('/profile/<username>') #using username as the variable to input into the function for the website
def profile(username):
    return "<h1>Hey there, %s!!!</h1>" % username

@app.route('/post/<int:post_id>') #variables with integers need to be called out as int within the app.route decorator. this is expecting an integer
def show_post(post_id):
    return "<h1>Post ID is %s!!!</h1>" % post_id


# start this web server. we need to kick off the website on the server. and then the website will start running
if __name__ == "__main__":  # its a quick check to make sure we only run the web server when the file is called directly
    app.run (debug=True)
