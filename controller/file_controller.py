# coding=utf-8
'some comment...'
from flask import Blueprint, request
from bootstrap_init import app
from common.exception import ServiceException, ErrorCode
from service.image_service import ImageService

__author__ = 'Jiateng Liang'

file_bp = Blueprint('file_bp', __name__)


@file_bp.route("/images", methods=['POST'])
def image_upload():
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1] in app.config.get('ALLOWED_EXTENSIONS')
    file = request.files['file']
    if file and allowed_file(file.filename):
        ImageService.upload_image(file.filename, app.config.get('UPLOAD_FOLDER'))
    else:
        raise ServiceException(ErrorCode.PARAM_ERROR, 'file format error')
