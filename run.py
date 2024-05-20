from flaskblog import create_app
from flask import current_app,g, request
import logging
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s: %(message)s',
    }},
    'handlers': {'file': {
        'class': 'logging.FileHandler',
        'filename': 'record.log',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})
#logging.basicConfig(filename='record.log', level=logging.DEBUG)

app = create_app()

#print(app.url_map)

with app.app_context():
    print("current app name", current_app)
    print("current app name", current_app.name)
    print("g ---", g)

with app.test_request_context():
    print('during with block')

if __name__ == '__main__':
    app.run(debug=True)
