import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from model import getAllAdmin, LoginModal



# make dev: export FLASK_ENV=development
# make dev: $env:FLASK_ENV=development
# powershell: $env:FLASK_APP="flask_app"
#cmd : set FLASK_APP = tidal
app = Flask(__name__)
CORS(app) # define and initialise cors.

# default route
@app.route("/")
def index():
  return {"message" : "ola...." }

@app.route("/dummy")
def dummy():
  return {"message" : "ola... dummy end point" }

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
  
  
  
if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
