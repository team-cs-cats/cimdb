

from flask import Flask, render_template
from flask import request, redirect

# This will eventually connect to the database, but for now it is not enabled
# from db_connector.db_connector import connect_to_database, execute_query

#create the web application
webapp = Flask(__name__)

#provide a route for the index of the webpage requests on the web application can be addressed
@webapp.route('/')
def index():
    return render_template("index.html")



