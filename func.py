import io
import json
import requests
import oracledb
from fdk import response

# 1. EXTRACT
def get_flight_data():
    url = "https://opensky-network.org/api/states/all?lamin=25.0&lomin=-106.0&lamax=36.0&lomax=-93.0"
    resp = requests.get(url)
    return resp.json().get('states', [])

# 2. TRANSFORM & LOAD
def load_data_to_oracle(flights):
    connection = oracledb.connect(
        user="ADMIN",
        password="0n@stR8l1n3U",
        dsn="AviationDB_high", 
        config_dir="/function/wallet",
        wallet_location="/function/wallet",
        wallet_password="Tij79268*"
    )
    
    cursor = connection.cursor()
    sql = """INSERT INTO FLIGHT_TELEMETRY 
             (ICAO24, CALLSIGN, ORIGIN_COUNTRY, LONGITUDE, LATITUDE, ALTITUDE, VELOCITY) 
             VALUES (:1, :2, :3, :4, :5, :6, :7)"""
             
    for flight in flights[:50]:
        icao24 = flight[0]
        callsign = flight[1].strip() if flight[1] else "UNKNOWN"
        country = flight[2]
        longitude = flight[5]
        latitude = flight[6]
        altitude = flight[7]
        velocity = flight[9]
        cursor.execute(sql, [icao24, callsign, country, longitude, latitude, altitude, velocity])
        
    connection.commit()
    cursor.close()
    connection.close()

# 3. THE CLOUD HANDLER
def handler(ctx, data: io.BytesIO = None):
    try:
        flights = get_flight_data()
        if flights:
            load_data_to_oracle(flights)
        return response.Response(
            ctx, response_data=json.dumps({"status": "Data loaded successfully"}),
            headers={"Content-Type": "application/json"}
        )
    except Exception as e:
        return response.Response(
            ctx, response_data=json.dumps({"error": str(e)}),
            headers={"Content-Type": "application/json"}
        )