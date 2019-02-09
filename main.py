from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for, session

import models as dbHandler


app = Flask(__name__)

# @app.route("/loginpage")
# def loginpage():
#     return render_template('login.html')

@app.route("/mainpage", methods=['POST', 'GET'])
def mainpage():
    vehicleNumber = 1007
    startTime = 100
    dailyOrders = dbHandler.getDailyRecords(vehicleNumber,startTime)
    return render_template('main_page.html', result = dailyOrders )

@app.route("/addOrderInfo", methods=['POST', 'GET'])
def addOrderInfo():
    if request.method=='POST':
        numoforders = request.form['numoforders']
        totalcost = request.form['totalcost']
        vehicleNumber = 1007
        dbHandler.insertDailyRecord(vehicleNumber,int(numoforders),int(totalcost))
        return redirect(url_for('mainpage'))
    else:
        return render_template('add_order.html')

if __name__ == "__main__":
    app.run(debug=True)