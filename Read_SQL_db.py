import pyodbc  # module for accessing ODBC databases
import pandas as pd

# connection data of SQL server and database
driver = 'DRIVER={SQL Server}'  # for MS SQL (driver is different for MySQL etc.)
server = 'mate-test-sqlserver.database.windows.net' 
database = 'TopBike' 
username = 'tanfolyam' 
password = 'vx#34T6k*E12'  

# connect
cnxn = pyodbc.connect(driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

# SQL query to pre-filter data
query = 'SELECT o.OrderDate, c.Country, od.LineTotal, p.ProductSubcategoryID \
FROM Customer c \
JOIN Orders o on c.CustomerID = o.CustomerID \
JOIN OrderDetail od on od.OrderID = o.OrderID \
JOIN Product p on p.ProductID = od.ProductID;'

# read the data from the SQL database based on the query
df = pd.read_sql(query, cnxn)

print(df)