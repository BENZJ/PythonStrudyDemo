# Django使用

## 基本命令
1. 创建项目
```bash
django-admin.py startproject learning_log
```
2. 运行项目
```bash
python manage.py runserver
```

3. 创建数据库
```bash
python manage.py migrate
```
4. 激活模型<br>
在setting.py中的INSTALLED_APPS中加入自己的应用名如下

  ```python
  INSTALLED_APPS = (
    'django.contrib.staticfiles',
    # 我的应用程序
    'learning_logs',
  )

  ```

5. 建立数据库模型</br>
在项目中的models.py中创建类继承django.db 里的models类，创建好类之后更新数据库

  ```bash
  python manage.py makemigrations your_app_name
  python manage.py migrate
  ```

6. 创建管理员账户</br>
```bash
python manage.py createsuperuser
```

7. 模版配置注意点
模版的html默认要放在templates文件夹下面才能访问没有templates需要自己创建。
