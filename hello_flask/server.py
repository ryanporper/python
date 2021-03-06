from flask import Flask, render_template

app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')
def success():
  return "Dojo!"

@app.route('/say/<string:word>')
def say(word):
    print(word)
    return "Hi, " + word

@app.route('/repeat/<int:num>/<string:word>') 
def repeat(num, word):
    return num * word

@app.route('/lists')
def render_lists():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("lists.html", users = users)

if __name__=="__main__":   
    app.run(debug=True)    
    