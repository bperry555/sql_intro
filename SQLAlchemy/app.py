from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

engine = create_engine("sqlite:///Resources/hawaii.sqlite?check_same_thread=False")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

app = Flask(__name__)

@app.route("/")
def welcome():
        return (
            "Welcome~!</br></br>"
            "Available Routes:<br/><br/>"
            "/api/v1.0/precipitation<br/>"
            "/api/v1.0/stations<br/>"
            "/api/v1.0/tobs<br/>"
            "/api/v1.0/<start>yyyy-mm-dd<br/>"
            "/api/v1.0/<start>yyyy-mm-dd/<end>yyyy-mm-dd<br/>"
        )

@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(Measurement.date, Measurement.prcp).all()
    return jsonify(results)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query( Station.name).all()
    return jsonify(results)

@app.route("/api/v1.0/tobs")
def tobs():
    tobs_last = dt.date(2017,8,23)
    tobs_first = (tobs_last - dt.timedelta(days=365))
    results = session.query(Measurement.date, Measurement.tobs). \
        filter(Measurement.station == 'USC00519281'). \
        filter(Measurement.date >= tobs_first).all()
    return jsonify(results)
# Instructions were unclear if we were to filter with the staion with the most tobs data.

@app.route("/api/v1.0/<start>")
def start_beg(start):
    result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    return jsonify(result)

@app.route("/api/v1.0/<start_date>/<end_date>")
def start_end(start_date, end_date):
    result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    return jsonify(result)

if __name__== "__main__":
    app.run(debug=True)