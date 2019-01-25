from flask import Flask
from flaskext.mysql import MySQL
import json
from flask import Response, request
from passlib.hash import sha256_crypt
import jwt


app = Flask(__name__)

def checkAuth(jwttoken):
	print(jwttoken)
	if (jwttoken):
		try:
			decoded= jwt.decode(jwttoken, 'memMEBER&&##Data$@#^&#@&#^@&#',  algorithms=['HS256'])
			return True
		except:
			return False
		return True
	else:
		return False

def encryptPassword(password):
	return sha256_crypt.hash(password)


def verifyPasswords(password, dbpassword):
	return sha256_crypt.verify(password, dbpassword)


# connection to mysql
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Newlife7'
app.config['MYSQL_DATABASE_DB'] = 'members'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/members', methods = ['GET'])
def membersList():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT firstName, lastName, reason_for_payment, amount, payment_months, date, received_by from membersForm;")
    returnData = []
    data = cursor.fetchall()
    for info in data:
        userObject = {"firstName": info[0],"lastName": info[1], "reason_for_payment": info[2], "amount": info[3], "payment_months": info[4],"date":info[5],"received_by": info[6]}
        returnData.append(userObject)
        jsonResult = json.dumps(returnData, indent=4, sort_keys=True, default=str)
	return Response(jsonResult, mimetype ='application/json')
    else:
	    return Response(json.dumps({"status": False, "message": "Token not valid"}), mimetype='application/json')


@app.route('/members', methods = ['POST'])
def addMembers():
    conn = mysql.connect()
    cursor = conn.cursor()

    data_members = json.loads(request.data)
    firstName = data_members.get('firstName', None)
    lastName = data_members.get('lastName', None)
    reason_for_payment = data_members.get('reason_for_payment', None)
    amount = data_members.get('amount', None)
    payment_months = data_members.get('payment_months', None)
    date = data_members.get('date', None)
    received_by = data_members.get('received_by', None)


    if not firstName:
        return Response(json.dumps({'status': False, 'message':'First Name is required'}), mimetype='application/json')
    if not lastName:
        return Response(json.dumps({'status': False, 'message':'Last Name is required'}), mimetype='application/json')
    if not reason_for_payment:
        return Response(json.dumps({'status': False,'message':'Reason for payment is required'}), mimetype='application/json')
    if not amount:
        return Response(json.dumps({'status': False, 'message':'Amount of payment is required'}), mimetype='application/json')
    try:
        cursor.execute("INSERT INTO membersForm (firstName, lastName, reason_for_payment, amount, payment_months, date, received_by) VALUE (%s,%s,%s,%s,%s,%s,%s)",(firstName, lastName, reason_for_payment, amount, payment_months, date, received_by))
        conn.commit()
        return Response(json.dumps({"status":True}), mimetype='application/json')
    except Exception, e:
       return Response(json.dumps({"status":False, 'message': str(e)}), mimetype='application/json')


@app.route('/login', methods = ['POST'])
def login():
    conn = mysql.connect()
    cursor = conn.cursor()

    data_members = json.loads(request.data)
    userName = data_members.get('userName', None)
    password = data_members.get('password', None)

    if not userName:
		return Response(json.dumps({"status": False, "message": "User Name Required"}), mimetype='application/json')

    if not password:
		return Response(json.dumps({"status": False, "message": "Password Required"}), mimetype='application/json')
    try:
		cursor.execute("SELECT * from membersForm WHERE userName = %s", (userName))
		info = cursor.fetchone()
		if info is None:
			return Response(json.dumps({"status": False, "message" : "User Name is not valid"}), mimetype='application/json')
		dbpassword = info[7]
		isValidPassword = verifyPasswords(password, dbpassword)
		if not isValidPassword:
			return Response(json.dumps({"status": False, "message" : "Invalid Password"}), mimetype='application/json')

		returnMembersData = {
            "firstName": info[0],
            "lastName": info[1], 
            "reason_for_payment": info[2], 
            "amount": info[3], 
            "payment_months": info[4],
            "date":info[5],
            "received_by": info[6]
        }
        	encoded = jwt.encode(returnMembersData, 'memMEBER&&##Data$@#^&#@&#^@&#', algorithm='HS256')

		return Response(json.dumps({"status": True, "token": encoded}), mimetype='application/json')
    except Exception as e:
		return Response(json.dumps({"status": False, "message": str(e)}), mimetype='application/json')

