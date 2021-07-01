import logging.config

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'handlers': {
            'file_handler': {
                'level': 'DEBUG',
                'filename': 'logconfig.log',
                'formatter': 'simple',
            }
        },
        'loggers': {
            'request': {
                'handlers': ['file_handler', ],
                'level': 'DEBUG',
                'propagate': False,
            }
        }
    }
}

logging.config.dictConfig(LOG_CONFIG)
REQUEST_LOGGER = logging.getLogger('request')
