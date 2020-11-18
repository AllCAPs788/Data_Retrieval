
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

 # Design a query to retrieve the last 12 months of precipitation data and plot the results
months = session.query(measure.date).order_by(measure.date.desc()).first()
months
#Ins_dates examples


#session.query(Invoices.BillingCountry).group_by(Invoices.BillingCountry).all()
# Calculate the date 1 year ago from the last data point in the database
query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
query_date
# Perform a query to retrieve the precipitation scores and dates
time_frame = session.query(measure.date, measure.prcp).filter(measure.date >= query_date).all()
time_frame
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
    prcp = session.query(measure.date, measure.prcp).filter(measure.date >= query_date).all()
    #copy query_date from other Jupyter file
    precipitation = {k:v for k,v in prcp }
    

    return jsonify(date: prcp)

@app.route("/api/v1.0/precipitation")
def temperature():
    """List all available api routes."""
    temp = session.query(measure.date, measure.tobs).filter(measure.date >= query_date).all()
    #copy query_date from other Jupyter file
    temperature = {k:v for k,v in temp }

    return jsonify(date:temp)
if __name__ == "__main__":
    app.run(debug=True)
#ravel, dictionary comprehensions