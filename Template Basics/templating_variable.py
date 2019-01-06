from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    some_variable = "Faiz"
    letters = list(some_variable)
    pup_dict = {'pup_name':'Sammy'}
    # Connecting to a template (html file)
    return render_template('templating_variable.html',my_variable = some_variable,letters=letters,pup_dict = pup_dict)

if __name__ == '__main__':
    app.run(debug=True)