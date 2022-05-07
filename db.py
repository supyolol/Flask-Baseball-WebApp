import pyodbc

def dbconnection():
    server = 'SERVER' # to specify an alternate port
    database = 'DATABASE'
    username = 'USERNAME'
    password = 'PASSWORD'
   

    cnxn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.9.so.1.1};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password,autocommit=True)

    c = cnxn.cursor()

    return c

