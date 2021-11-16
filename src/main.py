from flask import Flask
from flask import jsonify
from views.user import user_views


app = Flask(__name__)
app.debug = True


app.register_blueprint(user_views)

if __name__ == '__main__':
    app.run(debug=True)

