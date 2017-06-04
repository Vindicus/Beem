# import sqlalchemy for psql database connection
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker, exc

#### THIS IS REQUIRED FOR DATABASE CONNECTION#####
# Below will be uncommented after creating a database and tables
# from "database_file_name.py" import "table name"
#### TEMPORARILY COMMENTED #######################

#anti-forgery sessions for client and server communication flask modules
from flask import session as login_var
# A wrapper for user authentication used in a decorator
from functools import wraps

# other python modules
import os, time, random, string, httplib2, requests

####CONNECTS TO DATABASE FOR SESSION CONNECTION###
# engine = create_engine('psql')
#Base.metadata.bind = engine
#DBSession = sessionmaker(bind=engine)
#session = DBSession()
######TEMPORARILY COMMENTED#######################



app = Flask(__name__)

# decorator for user authentication
def required_login(f):
    @wraps(f)
    def login(*args, **kwargs):
        if 'username' not in login_var:
            return redirect(url_for('login', next =request.url))
        return f(*args, **kwargs)
    return login



# Use this if your running web server on cloud9
# if __name__ == '__main__':
#    app.secret_key = 'super_secret_key'
#    app.debug = True
#    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))


# Use this if running on local/virtual machine
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
