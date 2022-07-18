from flask import Flask, render_template, request, redirect

# from users import User
from flask_app.controllers import controller_users
from flask_app import app

if __name__=="__main__":
    app.run(debug=True)