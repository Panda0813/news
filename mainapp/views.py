from flask import Blueprint, Flask, session, render_template, request, redirect, url_for
from mainapp import models

blue = Blueprint('news',__name__)

def init_blue(app:Flask):  #指明传入的app是Flask对象
    app.register_blueprint(blue)  #定义初始化蓝图的app方法

@blue.route('/')
def index():
    return '主页<br>Hello, {}'.format(session.get('login_name'))

@blue.route('/login/<name>/')
def login(name):
    #登录的用户添加到session
    session['login_name'] = name

    return 'session 添加成功'

@blue.route('/initdb/')
def initDB():
    models.db.create_all()
    return '数据库已初始化完成'

@blue.route('/add/<string:title>/<int:ord_no>/')
def add(title,ord_no):
    cate = models.Category(title=title,ord_no=ord_no,origin_url='')

    #提交到数据库
    models.db.session.add(cate)
    models.db.session.commit()  #提交事务

    return '添加分类: {} 成功!'.format(title)

@blue.route('/all/<any(cate,article):name>/')
def all(name):
    if name == 'cate':
        return render_template('cate_list.html',
                               cates=models.Category.query.all())
    else:
        return '待开发'

@blue.route('/delete/<int:id>')
def deleteCate(id):
    q = models.Category.query.filter_by(id=id).first()
    print(q)
    models.db.session.delete(q)  #删除
    models.db.session.commit()
    return '{} 删除成功!'.format(q.title)

@blue.route('/update/<int:id>/<title>/<path:url>')
def updateCate(id,title,url):
    q = models.db.session.query(models.Category).filter_by(id=id).first()
    print(q)
    q.title = title
    q.origin_url = url

    models.db.session.add(q)  #更新信息
    models.db.session.commit()  #提交事务

    return '{} 信息已更新,地址 {}'.format(q.title,q.origin_url)

@blue.route('/getcate/<int:id>',methods=('GET','POST'))
def getcate(id):
    #q = models.db.session.query(models.Category).get(id)  #get查询
    try:
        q = models.Category.query.get(id)
        print(q.id,q.title)
    except:
        return '查无数据'
    if request.method == 'GET':
        return render_template('cate_edit.html',cate=q)
    else:
        q.title = request.form.get('title')
        q.origin_url = request.form.get('url')
        models.db.session.add(q)
        models.db.session.commit()
        return redirect('/all/cate/')

@blue.route('/allarticle/<int:cateid>/')
def allarticle(cateid):
    category = models.Category.query.get(cateid)
    articles = category.articles
    return render_template('article_list.html',articles=articles,cateid=cateid)

@blue.route('/addarticle/<int:cateid>/<articleid>/',methods=('GET','POST'))
def addarticle(cateid,articleid):
    try:
        article = models.Article.query.get(articleid)
        print(article)
    except:
        return '信息错误'
    if request.method == 'GET':
        if article:
            return render_template('article_edit.html',cateid=cateid,article=article)  #请求编辑
        else:
            return render_template('article_edit.html',cateid=cateid)  #请求添加
    else:
        if article:
            article.title = request.form.get('title')
            article.content = request.form.get('content')
            article.origin = request.form.get('origin')
        else:
            article = models.Article()
            article.title = request.form.get('title')
            article.content = request.form.get('content')
            article.origin = request.form.get('origin')
            article.cate_id = cateid

        models.db.session.add(article)  #添加
        models.db.session.commit()  #提交事务

        return redirect(url_for('news.allarticle',cateid=cateid))  #重定向到当前分类的所有博客

@blue.route('/delarticle/<int:cateid>/<int:articleid>')
def delarticle(cateid,articleid):
    q = models.Article.query.get(articleid)
    models.db.session.delete(q)
    models.db.session.commit()

    return redirect(url_for('news.allarticle',cateid=cateid))
