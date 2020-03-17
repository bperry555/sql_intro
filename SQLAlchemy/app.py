from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def welcome():
        return (
            f"Available Routes:<br/><br/>"
            f"/api/v1.0/precipitation<br/>"
            f"/api/v1.0/stations<br/>"
            f"/api/v1.0/tobs<br/>"
            f"/api/v1.0/<start><br/>"
            f"/api/v1.0/<start>/<end><br/>"
        )

@app.route("/api/v1.0/precipitation")
def precipitation():
    return "percipitation"

@app.route("/api/v1.0/stations")
def stations():
    return "stations"

@app.route("/api/v1.0/tobs")
def tobs()
    return "tobs"

@app.route("/api/v1.0/<start>")
def start()
    return "start"

@app.route("/api/v1.0/<start>/<end>")
def start_end()
    return "start/end"

if __name__== "__main__":
    app.run(debug=True)