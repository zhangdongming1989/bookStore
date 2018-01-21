# -*- coding: utf-8 -*-
import logging

from flask import request
from bookStore.mappings.order import Order
from bookStore.mappings.order_detail import OrderDetail
from bookStore.service.order.order import OrderService
from bookStore.views.api import exports
from bookStore.views import make_api_response


@exports('/order/query', methods=['GET'])
def query_user_info():
    """
    @api {POST} /order/query 查询用户信息
    """
    user_id = request.form('userid')
    orders = OrderService.order_query(user_id)

    if orders:
        return make_api_response(payload=orders)
    else:
        return make_api_response(message="用户不存在", statusCode=400)

@exports('/order/detail', methods=['GET'])
def update_user_info():
    """
    @api {POST} /order/detail 查询用户信息
    """
    # 获取参数
    order_id = request.form['orderid']
    order_detail = OrderService.order_detail(order_id)

    if orders_detail:
        return make_api_response(payload=order_detail)
    else:
        return make_api_response(message="订单不存在", statusCode=400)
