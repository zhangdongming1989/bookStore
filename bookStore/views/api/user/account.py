# -*- coding: utf-8 -*-
import logging

from flask import request
from flask_login import current_user, login_required

from bookStore import app
from bookStore.service.user.account import AccountService
from bookStore.views.api import exports
from bookStore.views import make_api_response


@exports('/account/query', methods=['POST'])
@login_required
def query_user_info():
    """
    @api {POST} /account/query 查询用户账户信息
    @apiGroup Users
    @apiVersion 0.0.1
    @apiDescription 用于查询用户资料
    @apiParam {String} user_id 用户id
    @apiParamExample {json} 请求样例：
                    {
                        "user_id": 123
                    }
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                   {
                        "status": "ok",
                        "payload":{
                            "realname": "132",
                            "username": "bs",
                            "phone": "pwd",
                            "mail": "xxx@xxx.com",
                            "nickname": "guest",
                            "gender": "23",
                            "password": "pwd",
                            "qq": "12312"
                        }
                    }
    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    # user_id = request.json['user_id']
    user_id = current_user.id
    app.logger.info(user_id)
    account_info = AccountService.account_query(user_id=user_id)

    if account_info:
        return make_api_response(payload=account_info)
    else:
        return make_api_response(message="用户不存在", statusCode=400)

