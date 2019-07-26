创建项目：
django-admin.py startproject project_name
创建app：
python manage.py startapp app_name

创建、更改数据库表：
# 1. 创建更改的文件
python manage.py makemigrations
# 2. 将生成的py文件应用到数据库
python manage.py migrate
# 3. 清空数据库
python manage.py flush
# 4. 导出导入数据
python manage.py dumpdata appname > appname.json
python manage.py loaddata appname.json

启动应用：
python manage.py runserver

创建超级管理员：
python manage.py createsuperuser
修改密码
python manage.py changepassword username
