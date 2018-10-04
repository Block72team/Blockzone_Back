# coding=utf-8
'some comment...'
import json

from flask import Blueprint, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

from common.exception import api, ServiceException, ErrorCode
from common.form_util import validate_form
from model.post import Post
from service.post_service import PostService
from common.model_util import model2dict, json_resp

__author__ = 'Jiateng Liang'

posts_bp = Blueprint('posts_bp', __name__)


@posts_bp.route('/<id>', methods=['GET'])
@api
def get_post_by_id(id):
    post = PostService.get_post_by_id(id)
    PostService.add_pv(id, 1)
    return json_resp(data=model2dict(post))


@posts_bp.route('/drafts/count', methods=['GET'])
@api
def count_drafts():
    cnt = PostService.count_drafts()
    data = {'num': cnt}
    return jsonify(json_resp(data=data))


@posts_bp.route('/new', methods=['POST'])
@api
def create_post():
    post = Post()
    try:
        data = request.get_data()
        data = json.loads(data)
        post.title = data['title']
        post.content = data['content']
        post.category_id = data['category_id']
        post.tag_ids = data['tag_ids']
        post.region = data['region']
        post.image_header_id = data['image_header_id']
    except Exception:
        raise ServiceException(ErrorCode.PARAM_ERROR, 'param error')
    post = PostService.insert_post(post)
    return jsonify(json_resp(data=model2dict(post)))
