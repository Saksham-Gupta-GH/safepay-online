import sys
import os

# Ensure the project root is on the Python path so that all modules
# (encryption, hashing, model_predict, etc.) can be imported by app.py.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import app

# Vercel expects the WSGI application to be exposed as `app`
# (the variable name matches the filename pattern Vercel looks for).
