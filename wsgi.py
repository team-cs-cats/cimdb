# filename: wsgi.py
 # this allows gunicorn to run on the server

from app import webapp

if __name__ == "__main__":
    webapp.run()