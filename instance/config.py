import os
class Config(object):
    
    DEBUG = False
    SECRET = os.getenv('SECRET') 

   
class DevelopmentConfig(Config):

    DEBUG = True
class TestingConfig(Config):
  
    TESTING = True
    DEBUG = True
app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}