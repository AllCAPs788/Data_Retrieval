
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


# reflect an existing database into a new model

Base.classes.keys()
# reflect the tables



# Save reference to the table (change names)
measure = Base.classes.measurement
station = Base.classes.station


# Flask Setup
#################################################
app = Flask(__name__)



@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """List all available api routes."""
    #prcp = session.query(measure.date, measure.prcp).filter(year statement).all()
    #copy query_date from other Jupyter file
    precipitation = {k:v for k,v in prcp }
    

    return jsonify(date: )


if __name__ == "__main__":
    app.run(debug=True)
#ravel, dictionary comprehensions