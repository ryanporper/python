from flask_app import app
# import every controller file
from flask_app.controllers import recipe_controller, user_controller
       
if __name__ == "__main__":
    app.run(debug=True)