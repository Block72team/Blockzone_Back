# coding=utf-8
__author__ = 'Jiateng Liang'


class Config(object):
    """
    Default setting
    """
    AUTHOR = 'Jiateng Liang'
    # App setting
    HTTP_HEAD = 'http://'
    HTTP_HOST = '127.0.0.1'
    HTTP_PORT = 5000
    SECRET_KEY = 'blockzone'
    WTF_CSRF_ENABLED = False
    # Database setting
    DB_USERNAME = 'root'
    DB_PASSWORD = ''
    DB_HOST = '127.0.0.1'
    DB_NAME = 'blockzone'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_NAME + '?charset=utf8'
    ENABLE_SQL_LOG = True

    # Log setting
    LOG_NAME = 'blockzone'
    LOG_CONSOLE = True  # 是否打印到控制台
    LOG_LEVEL = 'DEBUG'  # DEBUG INFO WARN ERROR
    LOG_PATH = '/Users/liangjiateng/Desktop/log.log'
    LOG_FORMAT = '%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s'
    LOG_DATE_FORMAT = "%a %d %b %Y %H:%M:%S"

    # Pagination setting
    PAGE_SMALL = 10
    PAGE_MEDIUM = 25
    PAGE_LARGE = 50



