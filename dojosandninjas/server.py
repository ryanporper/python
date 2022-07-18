from flask_app import app
# import every controller file
from flask_app.controllers import controller_dojos, controller_ninjas
       
if __name__ == "__main__":
    app.run(debug=True)