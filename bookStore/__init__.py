# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import default_settings

db = SQLAlchemy()

class Application(Flask):

    def __init__(self):
        super(Application, self).__init__(
            __name__, static_folder='../static'
        )
        self.config.from_object(default_settings)

        # 生产环境配置
        if 'APP_CONFIG' in os.environ:
            self.config.from_envvar('APP_CONFIG', silent=False)
        else:
            dev_cfg = os.path.abspath(os.path.join(
                os.path.basename(__file__), '../dev.cfg'))
            self.config.from_pyfile(dev_cfg, silent=True)

    def ready(self):
        db.init_app(self)

app = Application()
