from app import app
from app import config

application = app

if not config.DEBUG:
    debug = False
else:
    debug = True

if __name__ == '__main__':
    #app.run(debug=debug)
    app.run(debug=debug, host= '0.0.0.0')
