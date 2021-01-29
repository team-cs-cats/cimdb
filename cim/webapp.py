# webapp.py
from flask import Flask, render_template
from flask import request, redirect

# import these to handle user accounts
from flask import url_for, session
from flask_login import login_user, current_user, logout_user, login_required

# This will eventually connect to the database, but for now it is not enabled
# from db_connector.db_connector import connect_to_database, execute_query


#create the web application
webapp = Flask(__name__)


# Set up login manager to handle basic user authentication
login_manager = flask_login.LoginManager()
login_manager.init_app(webapp)


# Set up a mock set of user ids to use for our logins (this can be moved/replaced later)
users = {
'ali@cimdb.com': {'password': '12345'}
'asa@cimdb.com': {'password': '54321'}
}



#provide a route for the index of the webpage requests on the web application can be addressed
@webapp.route('/')
def index():
    """The webapp's landing page."""
    return render_template("index.html")

@webapp.route('/workorders')
@login_required
def workorders():
    """The webapp's page for work orders, which allows reviewing and adding work orders."""

    # if the current user is not authenticated, redirect the user to the landing page
    if not current_user.is_authenticated:
    	return redirect(url_for("cim.templates.index"))

    # otherwise, return the workorders page
    return render_template("workorders.html")

@webapp.route('/products')
@login_required
def products():
    """The webapp's page for viewing an employee's currently assigned products to assemble and QC."""
    return render_template("products.html")

@webapp.route('/inventory')
@login_required
def inventory():
    """The webapp's page for viewing the inventory.
    This allows the employee to review existing stock and order new stock of standard and special components."""
    return render_template("inventory.html")

@webapp.route('/user_management')
@login_required
def user_management():
    """The webapp's page for managing current users.
    This allows a manager to update information about current users."""
    return render_template("user_management.html")