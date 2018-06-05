from flask import Flask
from flask_session import Session
from mainapp import views, settings, models


def create_app():
    #创建app
    app = Flask(__name__)

    #配置app
    app.env = 'development'

    #从指定的类中获取属性配置app的config
    app.config.from_object(settings.Config)

    #相关的初始化
    views.init_blue(app)  #初始化蓝图
    Session(app)  #初始化session
    models.init_db(app)  #初始化模型数据库

    return app