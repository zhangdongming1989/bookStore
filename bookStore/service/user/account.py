# -*- coding:utf-8 -*-

from bookStore import db, app
from bookStore.mappings.account import Account

class AccountService():
    @staticmethod
    def account_query(user_id):
        """
        查询用户账户相关的信息
        """
        payload = {}
        if user_id:
            account = db.session.query(Account).filter_by(user_id=user_id).first()

            if account:
                payload['user_id'] = account.user_id
                payload['balance'] = account.balance
                payload['bonus_point'] = account.bonus_point
                payload['discount'] = account.discount

            return payload

        return None