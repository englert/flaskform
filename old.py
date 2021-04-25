import flask
from flask import render_template, request

print(__name__)
app = flask.Flask(__name__)

@app.route('/')
def form1():
    html = render_template('form1.html')
    return html

@app.route('/malac/')
def malac():
    i1 = request.args(i1)
    i2 = request.args(i2)
    print(i1, i2)
    return(f'{i1}   {i2}')

@app.route('/query-example')
def query_example():
    return 'Query String Example'

@app.route('/form-example')
def form_example():
    return '''
              <form method="POST">
                  <div><label>Language: <input type="text" name="language"></label></div>
                  <div><label>Framework: <input type="text" name="framework"></label></div>
                  <input type="submit" value="Submit">
              </form>'''

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

@app.route('/query')
def query():
    # if key doesn't exist, returns None
    language = request.args.get('language')

    # if key doesn't exist, returns a 400, bad request error
    framework = request.args['framework']

    # if key doesn't exist, returns None
    website = request.args.get('website')

    return f'''
              <h1>The language value is: {language}</h1>
              <h1>The framework value is: {framework}</h1>
              <h1>The website value is: {website}'''

if __name__ == '__main__':
    app.run('0.0.0.0')