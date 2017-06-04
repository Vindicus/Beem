import pip

def install(package):
    pip.main(['install', package])

# modules
if __name__ == '__main__':
    install('sqlalchemy')
    # install('psycopg2') using SQLite instead of postgresql for this project
    install('flask')
