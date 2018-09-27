# coding=utf-8
'some comment...'
from bootstrap_init import app

__author__ = 'Jiateng Liang'
from qiniu import Auth, put_file


class ImageService(object):
    @staticmethod
    def upload_image(file_name, file_path):

        q = Auth(app.config.get('ACCESS_KEY'), app.config.get('SECRET_KEY'))
        token = q.upload_token(app.config.get('BUCKET_NAME'))

        put_file(token, file_name, file_path)
