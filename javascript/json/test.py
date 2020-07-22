import json

from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request



app = Flask(__name__)

@app.route('/')
def hello():
    #return 'hello, world'
    return render_template('hello.html')


@app.route('/demo_file_array', methods=["GET","POST"])
def demo_file_array():
    if request.method == "GET":
        return render_template('array_or_list.html')
    else:
        mylist = ["John", "Mary", "Peter", "Sally"]
        return json.dumps(mylist)
        
@app.route('/demo_file_array_test', methods=["GET","POST"])
def demo_file_array_test():
    mylist = ["John", "Mary", "Peter", "Sally"]
    return json.dumps(mylist)

@app.route('/fetch_api', methods=["GET","POST"])
def fetch_api():
    if request.method == "GET":
        return render_template('fetch_api.html')
    else:
        mylist = ["John", "Mary", "Peter", "Sally"]
        return json.dumps(mylist)
        
@app.route('/fetch_api_test', methods=["GET","POST"])
def fetch_api_test():
    mylist = ["John", "Mary", "Peter", "Sally"]
    return json.dumps(mylist)    

@app.route('/demo_file')
def demo_file():
    import json
    myobj = {
        "name": "John stone",
        "age": 30,
        "city": "New York"
    }
    return json.dumps(myobj)
    #return jsonify(myobj)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
