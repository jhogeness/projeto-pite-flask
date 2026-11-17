from flask import Flask
from .models import db

def create_app(config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tarefas.db"
    app.config["SECRET_KEY"] = "chave-secreta-desenvolvimento"
    
    if config:
        app.config.update(config)
        
    db.init_app(app)
    
    from .controllers import bp
    app.register_blueprint(bp)
    
    with app.app_context():
        db.create_all()
        
    return app