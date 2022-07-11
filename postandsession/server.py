from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)  
app.secret_key = "supersecretkey"  

#display route
@app.route('/')          
def hello_world():
    name = "Ryan"
    return render_template("index.html", name = name)  

#action route
@app.route('/info', methods=['POST']) 
def info():
    print(f"You have just purchased a brand new {request.form['item']}")  

    session['ccn'] = request.form['card'][-4:]

    return redirect('/tracking')   

#display route
@app.route('/tracking')
def tracking():
    print(session['ccn'])

    if 'ccn' not in session:
        return redirect('/')

    return render_template("tracking.html")  

if __name__=="__main__":   
    app.run(debug=True)   