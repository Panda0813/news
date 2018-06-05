from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):  #传入app
    db.init_app(app)

    #创建migrate迁移对象
    Migrate(app,db)


class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(50),nullable=False,unique=True)
    #排序字段
    ord_no = db.Column(db.Integer,default=1)

    #类型关联的url
    origin_url = db.Column(db.String,nullable=True)

    #设置表名
    __tablename__ = 'news_category'

class Article(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(50),unique=True)
    content = db.Column(db.Text,nullable=True)
    origin = db.Column(db.String(50),default='网易新闻')

    #设置外键：主表表名.id
    cate_id = db.Column(db.Integer,db.ForeignKey('news_category.id'),nullable=True)
    # 为当前模型添加category属性,可以访问Category的所有属性
    # 同时返回给Category一个articles属性，可以访问Article的所有属性
    # lazy 懒加载，只有使用时才会调用的属性
    cate = db.relationship('Category',backref=db.backref('articles',lazy=True))

    __tablename__ = 'news_article'