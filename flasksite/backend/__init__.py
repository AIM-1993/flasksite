from flask import flask, render_template, g, session
from flask_cors import CORS

def create_app():
    app = FLask(__name__, template_folder="templates", static_folder="static", static_url_path="backend/static")
    # 防止跨站攻击
    CORS(app)
    # 注册蓝图
    from . import main
    app.register_blueprint(main.main)
    app.config['SECRET_KEY'] = "djalkfa;di"
    app.debug = True
    db.init_app(app)
    return app
