import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///eval.db")


@app.route("/")
def index():
    # Render template for index page
    return render_template("index.html")


@app.route("/ratings")
def ratings():
    # Render template for displaying all ratings

    # Display all data
    data = db.execute("SELECT *\
                       FROM eval\
                       ORDER BY last_name, class_name, year DESC")
    return render_template("ratings.html", data = data)