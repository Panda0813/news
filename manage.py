from flask_migrate import MigrateCommand

from mainapp import create_app
from flask_script import Manager

app = create_app()

manager = Manager(app)

# 命令行输入：python manage.py db -? 查看所有命令
# 常用命令：init初始化数据库环境
# migrate生成表的迁移计划
# upgrade执行新的迁移计划
# downgrade执行之前的迁移计划
manager.add_command('db',MigrateCommand)  #注册迁移命令

if __name__ == '__main__':
    manager.run()