#from api.manual_response import app
#from api.make_response_helper import app
from api.response_session import app

if __name__ == "__main__":
    app.run(debug = True)