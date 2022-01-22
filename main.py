import connexion

import logging
import coloredlogs
from flask_cors import CORS

import config

coloredlogs.install(fmt='%(levelname)-8s %(name)-8s : %(message)s')


app = connexion.App(__name__, specification_dir='openapi/')
app.add_api('contract.yaml', base_path='/api')

CORS(app.app)

if __name__ == '__main__':
    app.run(port=config.API_PORT)
