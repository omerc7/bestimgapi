import os


# Will raise KeyError if Env vars don't exsit
FACE_API_KEY = os.environ['FACE_API_KEY']
FACE_API_ENDPOINT = os.environ['FACE_API_ENDPOINT']

VALID_IMAGE_FORMATS = {'jpg', 'png', 'jpeg'}

LOG_FILE = 'BestImgAPI.log'
# LOGGING_CONFIG = {
#     'version': 1,
#     'loggers': {
#         '': {
#             'level': 'INFO',
#             'handlers': ['rotating_file_handler'],
#         },
#         'bestimgapp': {
#             'level': 'INFO',
#             'handlers': ['rotating_file_handler'],
#             'propagate': False,
#         }
#     },
#     'handlers': {
#         'rotating_file_handler': {
#             'level': 'DEBUG',
#             'formatter': 'debug',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': LOG_FILE,
#             'mode': 'a',
#             'maxBytes': 1048576,
#             'backupCount': 10
#         },
#     },
#     'formatters': {
#         'debug': {
#             'format': '%(asctime)s-%(levelname)s-%(name)s::%(module)s|%(lineno)s:: %(message)s'
#         },
#     },
# }

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'root': {
            'level': 'DEBUG',
            'handlers': ['wsgi']
        },
        'bestimgapp': {
            'level': 'INFO',
            'handlers': ['wsgi'],
            'propagate': False,
        }
    }
}
