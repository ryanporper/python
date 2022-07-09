from flask import Flask, render_template

app = Flask(__name__)    

@app.route('/')          
def render_board():
    return render_template("board.html")  


@app.route('/<int:num>') 
def alt_board(num):
    return render_template("altboard.html", num = num)

if __name__=="__main__":   
    app.run(debug=True)  