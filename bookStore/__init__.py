# -*- coding: utf-8 -*-

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

    def ready(self):
        pass

app = Application()
