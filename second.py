def funct1(year,engineHP,engineCylinders,numberofDoors,highwaympg,cityMPG,popularity,engineFuelType_n,transmissionType_n,drivenWheels_n,vehicleSize_n,vehicleStyle_n):
    #importing libraries
    import pandas as pd
    import numpy as np
    from sklearn import linear_model
    
    df = pd.read_csv("car2.csv")
    #drop unwanted coloumns from dataset
    target = df.MSRP

    #converting string data to numerical data
    from sklearn.preprocessing import LabelEncoder
    labelencode = LabelEncoder()

    df['EngineFuelType_n'] = labelencode.fit_transform(df['EngineFuelType'])
    df['TransmissionType_n'] = labelencode.fit_transform(df['TransmissionType'])
    df['DrivenWheels_n'] = labelencode.fit_transform(df['DrivenWheels'])
    df['VehicleSize_n'] = labelencode.fit_transform(df['VehicleSize'])
    df['VehicleStyle_n'] = labelencode.fit_transform(df['VehicleStyle'])

    inputdata = df.drop(['Make','EngineFuelType','TransmissionType','DrivenWheels','MarketCategory','VehicleSize','VehicleStyle','MSRP'],axis=1)
    inputdata

    inputdata.fillna(0, inplace=True)

    # train the data
    model = linear_model.LinearRegression()
    model.fit(inputdata,target)

    value = 10
    value = model.predict([[year,engineHP,engineCylinders,numberofDoors,highwaympg,cityMPG,popularity,engineFuelType_n,transmissionType_n,drivenWheels_n,vehicleSize_n,vehicleStyle_n]])
    return value