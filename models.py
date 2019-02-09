import sqlite3 as sql
import time

def insertDailyRecord(vehicleNum,numOfOrders,totalCost):
    con = sql.connect("ERP_db.db")
    cur = con.cursor()
    insertStatement = "INSERT INTO daily_orders (vehicle_num,time_stamp,num_of_orders,total_cost) VALUES (?,?,?,?)"
    cur.execute(insertStatement, (vehicleNum,time.time(),numOfOrders,totalCost))
    print(insertStatement)
    con.commit()
    con.close()


def deleteDailyRecord(vehicleNum,timeStamp):
    con = sql.connect("ERP_db.db")
    cur = con.cursor()
    deleteStatement = "DELETE FROM daily_orders where time_stamp = "+ timeStamp
    print(deleteStatement)
    cur.execute(deleteStatement)
    con.commit()
    con.close()

def getDailyRecords(vehicleNum, startTime):
    con = sql.connect("ERP_db.db")
    cur = con.cursor()
    getStatement = "SELECT * FROM daily_orders where vehicle_num = " + str(vehicleNum) + " and time_stamp >= " + str(startTime) + ""
    print(getStatement)
    cur.execute(getStatement)
    ordersList = cur.fetchall()
    con.close()
    return ordersList
