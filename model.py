from config import func

connection = func()
cursor = connection.cursor()



# when login, first get user email from customer register
# use that email and customer id to cross-check with customer_id
class LoginModal:
  def __init__(self, email, password):
    self.email = email
    self.password = password
    self.customer = ''
    
  # get customer id and email
  def getCustomerEmail(self):
    try:
      q = f"SELECT * FROM CustomerRegister WHERE `email`='{self.email}'"
      cursor.execute(q)
      data = cursor.fetchone()
      return data 
    except Exception as err:
      print(err)
      return False
  # cross check customer id and email, and password
  def getAdminUser(self):
    try:
      data = self.getCustomerEmail()
      if data:
        data = list( data )
        f_data = self.makeDictCustomer(data)
        q = f"SELECT * FROM UserAdminData WHERE `customer_id`='{data[0]}' AND `user_password`='{self.password}'"
        cursor.execute(q)
        data1 = cursor.fetchone()
        if cursor.rowcount > 0:
          # print( data1 )
          f_data.update( self.makeDictUserAdmin( data1 ) )
          return f_data
        # wrong email
        else:
          return "Pleas Provide A Correct Email"
      else:
        return "Not User Found..."
    except Exception as err:
      print(err)
      return err
      
  # format data and return
  def makeDictCustomer( self, data ):
    data_ = {
      "customer_id": data[0],
      "customer_name": data[1],
      "email": data[2],
      "phone": data[3],
      "billing_address": data[4],
      "contact_person": data[5],
      "customer_status": data[6],
    }
    return data_
  
  # format data from user admin table, into dict type, json like 
  def makeDictUserAdmin( self, data ):
    # don't think it's secure to pass user password to front-end.
    # "user_password": data[2],
    data_ = {
      "user_id": data[0],
      "date_created": data[3],
      "user_status": data[4],
      "roles": data[5],
      "last_seen": data[6],
      "user_ip": data[7],
    }
    return data_
      
      
      
      
  
  
def getAllAdmin():
  try:
    q = f"SELECT * FROM UserAdminData"
    cursor.execute(q)
    data = cursor.fetchone()
    print( data )
  except Exception as err:
    print(err)








