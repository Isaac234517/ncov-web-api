from flask import Flask, request, make_response
from flask import Flask
import json 
import sys
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/api/area")
def area():
    province = request.args.get('province')
    with open("./json_data/DXYArea-TimeSeries.json", encoding="utf-8") as f:
        data = json.load(f)
    target_data =[t for t in data if t["provinceName"] == province]
    #return jsonify(targetData)
    json_str = json.dumps(target_data, ensure_ascii = False)
    response = make_response(json_str)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['mimetype'] = 'application/json'
    response.status_code = 200
    return response

@app.route("/api/overall")
def overall():
    with open("./json_data/DXYOverall-TimeSeries.json", encoding="utf-8") as f:
        data = json.load(f)
    json_str = json.dumps(data, ensure_ascii = False)
    response = make_response(json_str)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['mimetype'] = 'application/json'
    response.status_code = 200
    return response

@app.route("/api/area_current")
def area_current():
    province = request.args.get('province')
    with open("./json_data/DXYArea.json", encoding="utf-8") as f:
        data = json.load(f)
    data = data["results"]
    target_data =[t for t in data if t["provinceName"] == province]
    #return jsonify(targetData)
    json_str = json.dumps(target_data, ensure_ascii = False)
    response = make_response(json_str)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['mimetype'] = 'application/json'
    response.status_code = 200
    return response

@app.route("/api/overall_current")
def overall_current():
    with open("./json_data/DXYOverall.json", encoding="utf-8") as f:
        data = json.load(f)
    data = data["results"]
    json_str = json.dumps(data, ensure_ascii = False)
    response = make_response(json_str)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['mimetype'] = 'application/json'
    response.status_code = 200
    return response

@app.route("/api/all_cases")
def all_cases():
    with open("./json_data/DXYArea.json", encoding="utf-8") as f:
        data = json.load(f)
    json_str = json.dumps(data, ensure_ascii = False)
    response = make_response(json_str)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['mimetype'] = 'application/json'
    response.status_code = 200
    return response
   

@app.route('/timeseries')
def timeseries():
    return "Hello"
