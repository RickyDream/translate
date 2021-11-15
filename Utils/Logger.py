# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/1/7 15:17
# __fileName__ : GoldenCoordinateV2 Logger.py
# __devIDE__ : PyCharm


import logging.config
import logging
from Utils import Contants

logging_config_dict = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'console': {
            'format': Contants.LogFormatterDebug,
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'file': {
            'format': Contants.LogFormatter,
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'filters': {
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'console'
        },
        # maxBytes=0, backupCount=0, encoding=None
        # 'file': {
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': Contants.LogFile,
        #     'maxBytes': 1024*1024*2,
        #     'backupCount': 2000,
        #     'encoding': 'utf-8',
        #     'level': 'INFO',
        #     'formatter': 'file'
        # }

    },
    'loggers': {
        'app': {
            'level': 'DEBUG',
            'handlers': ['console']
        }
    }
}
# 'handlers': ['console', 'file']
logging.config.dictConfig(logging_config_dict)
logger = logging.getLogger('app')



