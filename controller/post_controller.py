# coding=utf-8
'some comment...'
from flask import Blueprint

from common.exception import api
from service.post_service import PostService
from common.model_util import model2dict, json_resp

__author__ = 'Jiateng Liang'

posts_bp = Blueprint('posts_bp', __name__)


@posts_bp.route('/<id>')
@api
def get_post_by_id(id):
    post = PostService.get_post_by_id(id)
    PostService.add_pv(id, 1)
    return json_resp(data=model2dict(post))



