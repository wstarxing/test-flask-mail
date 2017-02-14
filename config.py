# -*- coding: UTF-8 -*-
class Config:

    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'example@qq.com'
    MAIL_PASSWORD = 'password'
    MAIL_DEFAULT_SENDER = 'username'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    # 'testing': TestingConfig,
    # 'production': ProductionConfig,
    #  'heroku': HerokuConfig,
    #  'unix': UnixConfig,

    'default': DevelopmentConfig
}