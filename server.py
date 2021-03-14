from flask import Flask, render_template
import pyodbc
import pandas

import requests



# Specifying the ODBC driver, server name, database, etc. directly
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=MyKitchen;UID=sa;PWD=password')


# Create a cursor from the connection
cursor = cnxn.cursor()

# This is just an example that works for PostgreSQL and MySQL, with Python 2.7.
cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
cnxn.setencoding(encoding='utf-8')



cursor.execute("select * from BigFridge")
all_rows = cursor.fetchall()
Data = pandas.DataFrame(all_rows)
list_of_data = Data.values.tolist()

names = []
for item in list_of_data:
    tuple_thing =  item[0]
    item_name = tuple_thing[1]
    names.append(item_name)






app = Flask(__name__)


@app.route('/')
def home():

    return render_template("index.html", navigation=names)


if __name__=="__main__":
    app.run(debug=True)