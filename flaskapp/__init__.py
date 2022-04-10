from flask import Flask
from datetime import datetime

def create_app(config=None):

    # init app
    app = Flask(__name__)

    # load config, if passed in
    if config:
        app.config.update(**config)
    
    # define an endpoint
    @app.get("/")
    def index():
        return f"""
        <p>Hello World!</p>
        <p>The current time is: {datetime.now()}</p>
        """

    # return
    return app