# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)

@app.route('/')
@app.route('/query-example')
def query_example():
    language  = request.args.get('language')
    framework = request.args.get('framework')
    website   = request.args.get('website')
    return f'''<h1>The language value is: {language}</h1>
               <h1>The framework value is: {framework}</h1>
               <h1>The website value is: {website}'''
#   http://127.0.0.1:5000/query-example?language=Python&framework=Flask&website=www.cica.hu

@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return f'''
                  <h1>The language value is: {language}</h1>
                  <h1>The framework value is: {framework}</h1>'''
        
    elif request.method == 'GET':
        return f'''
            <form method="POST">
                <div><label>Language: <input type="text" name="language"></label></div>
                <div><label>Framework: <input type="text" name="framework"></label></div>
                <input type="submit" value="OK">
            </form>'''

@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()
    language = request_data['language']
    framework = request_data['framework']
    # two keys are needed because of the nested object
    python_version = request_data['version_info']['python']
    # an index is needed because of the array
    example = request_data['examples'][0]
    boolean_test = request_data['boolean_test']

    return f'''
        The language value is: {language}
        The framework value is: {framework}
        The Python version is: {python_version}
        The item at index 0 in the example list is: {example}
        The boolean value is: {boolean_test}'''

if __name__ == '__main__':
    app.run('0.0.0.0')