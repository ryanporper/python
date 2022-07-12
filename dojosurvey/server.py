from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)  
app.secret_key = "supersecretkey"  

#display route
@app.route('/')          
def hello_world():
    return render_template("index.html")  

#action route
@app.route('/process', methods=['POST']) 
def process():

    session['name'] = request.form['name']
    session['loc'] = request.form['loc']
    session['lang'] = request.form['lang']
    session['comment'] = request.form['comment']

    return redirect('/result')   

#display route
@app.route('/result')
def result():
    # checks for name because if there is no name info then surely they didn't fill out the form
    if 'name' not in session:
        return redirect('/')

    return render_template("result.html")  

if __name__=="__main__":   
    app.run(debug=True)   