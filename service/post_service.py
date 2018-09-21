# coding=utf-8
'some comment...'
from datetime import datetime

__author__ = 'Jiateng Liang'
from bootstrap_init import db
from model.post import Post
from common.exception import ServiceException, ErrorCode
from common.page_util import PageUtil


class PostService(object):
    ASC = 1
    DESC = 2

    @staticmethod
    def get_post_by_id(post_id):
        post = Post.query.filter(Post.id == post_id).first()
        if post is None:
            raise ServiceException(ErrorCode.NOT_FOUND, 'Post id = %s not found' % post_id)

    @staticmethod
    def count_posts_by_category_id(category_id):
        return Post.query.filter_by(Post.category_id == category_id).count()

    @staticmethod
    def count_posts_by_tag_id(tag_id):
        return Post.query.filter_by(Post.tag_ids.like('%' + tag_id + '%')).count()

    @staticmethod
    def count_posts_by_region(region):
        return Post.query.filter_by(Post.region == region).count()

    @staticmethod
    def insert_post(post):
        length = len(post.content)
        post.sub_content = post.content[0:min(200, length)] + '...'
        db.session.add(post)
        db.session.commit()

    @staticmethod
    def add_likes(post_id, cnt):
        post = PostService.get_post_by_id(post_id)
        post.likes += cnt
        post.update_time = datetime.now()
        db.session.add(post)
        db.session.commit()

    @staticmethod
    def add_pv(post_id, cnt):
        post = PostService.get_post_by_id(post_id)
        post.pv += cnt
        post.update_time = datetime.now()
        db.session.add(post)
        db.session.commit()

    @staticmethod
    def list_posts_by_page_order_by_time_filter_by_category_id(page, page_size, category_id, order=DESC):
        cnt = PostService.count_posts_by_category_id(category_id)
        page_util = PageUtil(page, page_size, cnt)
        if order == PostService.DESC:
            posts = Post.query().order_by(Post.create_time.desc()).slice(page_util.get_start(),
                                                                         page_util.get_end()).all()
        else:
            posts = Post.query().order_by(Post.create_time.asc()).slice(page_util.get_start(),
                                                                        page_util.get_end()).all()
        return posts

    @staticmethod
    def list_posts_by_page_order_by_pv_filter_by_category_id(page, page_size, category_id, order=DESC):
        cnt = PostService.count_posts_by_category_id(category_id)
        page_util = PageUtil(page, page_size, cnt)
        if order == PostService.DESC:
            posts = Post.query().order_by(Post.pv.desc()).slice(page_util.get_start(),
                                                                page_util.get_end()).all()
        else:
            posts = Post.query().order_by(Post.pv.asc()).slice(page_util.get_start(),
                                                               page_util.get_end()).all()
        return posts

    @staticmethod
    def list_posts_by_page_order_by_time_filter_by_tag_id(page, page_size, tag_id, order=DESC):
        cnt = PostService.count_posts_by_tag_id(tag_id)
        page_util = PageUtil(page, page_size, cnt)
        if order == PostService.DESC:
            posts = Post.query().order_by(Post.create_time.desc()).slice(page_util.get_start(),
                                                                         page_util.get_end()).all()
        else:
            posts = Post.query().order_by(Post.create_time.asc()).slice(page_util.get_start(),
                                                                        page_util.get_end()).all()
        return posts

    @staticmethod
    def list_posts_by_page_order_by_pv_filter_by_tag_id(page, page_size, tag_id, order=DESC):
        cnt = PostService.count_posts_by_tag_id(tag_id)
        page_util = PageUtil(page, page_size, cnt)
        if order == PostService.DESC:
            posts = Post.query().order_by(Post.pv.desc()).slice(page_util.get_start(),
                                                                page_util.get_end()).all()
        else:
            posts = Post.query().order_by(Post.pv.asc()).slice(page_util.get_start(),
                                                               page_util.get_end()).all()
        return posts

    @staticmethod
    def list_posts_by_page_order_by_time_filter_by_region(page, page_size, region, order=DESC):
        cnt = PostService.count_posts_by_region(region)
        page_util = PageUtil(page, page_size, cnt)
        if order == PostService.DESC:
            posts = Post.query().order_by(Post.create_time.desc()).slice(page_util.get_start(),
                                                                         page_util.get_end()).all()
        else:
            posts = Post.query().order_by(Post.create_time.asc()).slice(page_util.get_start(),
                                                                        page_util.get_end()).all()
        return posts

    @staticmethod
    def list_posts_by_page_order_by_pv_filter_by_region(page, page_size, region, order=DESC):
        cnt = PostService.count_posts_by_region(region)
        page_util = PageUtil(page, page_size, cnt)
        if order == PostService.DESC:
            posts = Post.query().order_by(Post.pv.desc()).slice(page_util.get_start(),
                                                                page_util.get_end()).all()
        else:
            posts = Post.query().order_by(Post.pv.asc()).slice(page_util.get_start(),
                                                               page_util.get_end()).all()
        return posts
