from flask import Flask, render_template, request
import second as s

app = Flask(__name__)

@app.route("/")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result",methods = ['post','get'])
def result():
    output = request.form.to_dict()
    year = float(output['year'])
    engineHP = float(output['engineHP'])
    engineCylinders = float(output['engineCylinders'])
    numberofDoors = float(output['numberofDoors'])
    highwaympg = float(output['highwaympg'])
    cityMPG = float(output['cityMPG'])
    popularity = float(output['popularity'])
    
    engineFuelType_n = output['engineFuelType_n']
    if engineFuelType_n == 'diesel':
        engineFuelType_n = float(1)
    elif engineFuelType_n == 'petrol':
        engineFuelType_n = float(2)
    else:
        engineFuelType_n = float(3)

    transmissionType_n = output['transmissionType_n']
    if transmissionType_n == 'Manual':
        transmissionType_n = float(1)
    else:
        transmissionType_n = float(2)
    

    drivenWheels_n = output['drivenWheels_n']
    if drivenWheels_n == 'all wheel drive':
        drivenWheels_n = float(2)
    else:
        drivenWheels_n = float(1)


    vehicleSize_n = output['vehicleSize_n']
    if vehicleSize_n == 'Compact':
        vehicleSize_n = float(1)
    elif vehicleSize_n == 'Midsize':
        vehicleSize_n = float(2)
    else:
        vehicleSize_n = float(3)


    vehicleStyle_n = output['vehicleStyle_n']
    if vehicleStyle_n == 'Sedan':
        vehicleStyle_n = float(1)
    elif vehicleStyle_n == 'Wegon':
        vehicleStyle_n = float(2)
    else:
        vehicleStyle_n = float(3)

    res = s.funct1(year,engineHP,engineCylinders,numberofDoors,highwaympg,cityMPG,popularity,engineFuelType_n,transmissionType_n,drivenWheels_n,vehicleSize_n,vehicleStyle_n)
    return render_template("index.html", res=res)

if __name__ == "__main__":
	app.run(debug= True)

