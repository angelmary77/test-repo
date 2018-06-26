import pyodbc


con = pyodbc.connect('DRIVER={FreeTDs};SERVER=Vega\sql2008R2inst;UID=sa;PWD=Wy0ming-12')
cur = con.cursor()
print cur
# rows = cur.execute("select * from Qubecentral.dbo.screens").fetchall()

# params = ("2017-12-01 00:00:00.000","2017-12-31 23:59:59.999")
# rows = cur.execute("{CALL [Qubecentral].[dbo].[GenerateKDMLogData] (?,?)}", params).fetchall()