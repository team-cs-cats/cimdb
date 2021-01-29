# webapp.py
from flask import Flask, render_template
from flask import request, redirect

# This will eventually connect to the database, but for now it is not enabled
# from db_connector.db_connector import connect_to_database, execute_query

#create the web application
webapp = Flask(__name__)

#provide a route for the index of the webpage requests on the web application can be addressed
@webapp.route('/')
def index():
    """The webapp's landing page."""
    return render_template("index.html")

@webapp.route('/workorders')
def workorders():
    """The webapp's page for work orders, which allows reviewing and adding work orders."""
    return render_template("workorders.html")

@webapp.route('/products')
def products():
    """The webapp's page for viewing an employee's currently assigned products to assemble and QC."""
    return render_template("products.html")

@webapp.route('/inventory')
def inventory():
    """The webapp's page for viewing the inventory.
    This allows the employee to review existing stock and order new stock of standard and special components."""
    return render_template("inventory.html")

@webapp.route('/user_management')
def user_management():
    """The webapp's page for managing current users.
    This allows a manager to update information about current users."""
    return render_template("user_management.html")