# -*- coding: utf-8 -*-
from bookStore import db
from bookStore.mappings.order import Order
from bookStore.mappings.order_detail import order_detail

class OrderService():

    @staticmethod
    def order_query(uid):
        """
        根据用户名查询 全部order
        """
        payload = {}
        if uid:
            sql = """
            SELECT
                *
            FROM order
            WHERE user_id = :user_id
            ORDER BY id DESC
            """
            rows = db.session.execute(sql, {"user_id": uid}).fetchall()
            for row in rows:
                order = row.__dict__
                payload[row.order_id] = order
            return payload

        raise NotImplementedError('不支持的查询方式')

    @staticmethod
    def order_detail_query(order_id)
        """
        根据订单名查询 订单的详细书目信息
        """
        payload = {}
        if uid:
            sql = """
            SELECT
                *
            FROM order_detail
            WHERE order_id = :order_id
            ORDER BY id DESC
            """
            rows = db.session.execute(sql, {"order_id": order_id}).fetchall()
            for row in rows:
                order_detail = row.__dict__
                payload[row.book_name] = order_detail
            return payload

        raise NotImplementedError('不支持的查询方式')