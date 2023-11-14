"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
from flask_pymongo import PyMongo
import arrow
import acp_times
import config

import logging

app = flask.Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/brevets"
mongo = PyMongo(app)
CONFIG = config.configuration()


###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times", methods=['GET', 'POST'])
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))    
    
    time = request.args.get('time', type=str)
    dist = request.args.get("dist", 0, type=float)
    arrow_time = arrow.get(time, 'YYYY-MM-DDTHH:mm')

    open_time = acp_times.open_time(km, dist, arrow_time).format('YYYY-MM-DDTHH:mm')
    close_time = acp_times.close_time(km, dist, arrow_time).format('YYYY-MM-DDTHH:mm')

    # Insert control times into MongoDB
    db.control_times.insert_one({
        "km": km,
        "dist": dist,
        "time": time,
        "open": open_time,
        "close": close_time
    })

    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)


#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")



