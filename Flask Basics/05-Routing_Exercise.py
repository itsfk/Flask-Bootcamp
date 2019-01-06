# Set up your imports here!
# import ...
from flask import Flask
app = Flask(__name__)


@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return '<h1> Welcome to latin Puppy page </h1>'
    

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!
    pupname = ''
    if name[-1] =='y':
        pupname = name[:-1]+'iful'
        print(pupname)
    else:
        pupname = name + 'y'
    return "<h1>Hi {}! Your puppylatin name is {} </h1>".format(name,pupname)
    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    

if __name__ == '__main__':
    # Fill me in!
    app.run()
