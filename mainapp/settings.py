from redis import Redis
import pymysql
class Config():
    DEBUG = True  #调试模式
    SECRET_KEY = 'abchello123321'
    SESSION_TYPE = 'redis'

    SESSION_REDIS = Redis(host='10.35.163.30',port=6379,db=1)

    #配置数据库链接
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@10.35.163.30:3306/newsflask'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///D:/python/news/news.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False