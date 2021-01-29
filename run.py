# filename: run.py
# description: When executed, imports the CIM webapp and runs it on local host, port 5000 


# imports the os
import os

# eventually this will import the database connection
#from db_connector.sample import app

# import the `webapp` Flask instance created in `webapp.py` in the `cim` directory
from cim.webapp import webapp


if __name__ == "__main__":
	port_number = 5000
	print(f'Local server running on port {port_number}.')
	port = int(os.environ.get("PORT", port_number))
	webapp.run(debug=True, host='0.0.0.0', port=port)

	