import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from model import getAllAdmin, LoginModal



# powershell: $env:FLASK_APP="index"
#cmd : set FLASK_APP = tidal
app = Flask(__name__)
CORS(app) # define and initialise cors.

# default route
@app.route("/")
def index():
  getAllAdmin()
  return {"message" : "ola...." }

# login end points
@app.route("/login", methods=['POST', 'GET'] )
def login():
  cors = CORS(app, resources={r"/*": {"origins": '*'}})
  if request.method == 'POST':
    data = request.json
    print( data )
    if data['email'] and data['password']:
      obj = LoginModal( data['email'], data['password'] )
      res = obj.getAdminUser()
      # print( res )
      return jsonify({"Message": res } )
    else:
      return jsonify({"Message":"Passed Empty Data"} )
  else:
    return jsonify({"message": "Not Post Data"})