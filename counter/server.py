from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)  
app.secret_key = "supersecretkey"  

#display route
@app.route('/')          
def index():
    if 'counter' in session:
        session['counter'] += 1

    return render_template("index.html")  

@app.route('/destroy_session')
def destroy_session():
    session['counter'] = 0
    return redirect('/')

@app.route('/plustwo')
def plustwo():
    # +1 because defualt route already adds 1 so 1+1=2 
    session['counter'] += 1
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    
    