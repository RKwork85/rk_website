#encoding: utf-8
import os
# 数据库链接配置
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'rkoa_course'
USERNAME = 'rkwork'
PASSWORD = 'rkwork'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True


#邮箱配置信息
MAIL_SERVER ="smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME ="3330867560@qq.com"
MAIL_PASSWORD ="qdgkzrnnnhuqdaac"
MAIL_DEFAULT_SENDER ="3330867560@qq.com"

# SECRET_KEY = os.urandom(24)
SECRET_KEY = "fafadgrawewga"