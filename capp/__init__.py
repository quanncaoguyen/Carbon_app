from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

application = Flask(__name__)

# Allow running locally without needing every production environment variable
application.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

# Prefer an explicit DATABASE_URL / RDS config, otherwise fall back to the local sqlite DB.
db_url = os.environ.get('DATABASE_URL')
if not db_url and os.environ.get('RDS_USERNAME'):
    db_url = (
        f"postgresql://{os.environ.get('RDS_USERNAME')}:{os.environ.get('RDS_PASSWORD', '')}"
        f"@{os.environ.get('RDS_HOSTNAME')}/{os.environ.get('RDS_DB_NAME')}"
    )
if not db_url:
    # sqlite file under repo for quick local testing
    db_url = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'site.db')}"

application.config['SQLALCHEMY_DATABASE_URI'] = db_url
application.config['SQLALCHEMY_BINDS'] = {'transport': db_url}
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager = LoginManager(application)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)
