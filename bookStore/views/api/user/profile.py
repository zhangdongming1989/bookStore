# -*- coding: utf-8 -*-
import logging

from flask import request
from bookStore.service.user.user import UserService
from bookStore.views.api import exports
from bookStore.views import make_api_response


@exports('/profile/query', methods=['POST'])
def query_user_info():
    """
    @api {POST} /profile/query 查询用户信息
    """
    username = request.form('username')
    userinfo = UserService.query_user(username=username)

    if result:
        return make_api_response(payload=userinfo)
    else:
        return make_api_response(message="用户不存在", statusCode=400)

@exports('/profile/update', methods=['POST'])
def update_user_info():
    """
    @api {POST} /profile/query 查询用户信息
    """
    # 获取参数
    user_name = request.form['username']
    display_name = request.form['nickname']
    real_name = request.form['realname']
    gender = request.form['gender']
    mail = request.form['mail']
    phone = request.form['phone']
    qq = request.form['qq']

    userinfo = {
        'username': user_name,
        'nickname': display_name,
        'realname': real_name,
        'password': password,
        'gender': gender,
        'mail': mail,
        'phone': phone
        'qq': qq
    }
    # 创建用户的操作
    ok = UserService.create_account(userinfo)
    if ok:
        db.commit_all()
    else:
        err.message = '创建用户遇到错误'
    return make_api_response()
