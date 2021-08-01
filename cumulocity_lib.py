import requests
import json
import datetime
import time
from requests.auth import HTTPBasicAuth

base_url = "https://uowd.cumulocity.com" 
username = "greenergi.business@gmail.com" 
password = "ZobaloFTW1" 
device_id = "4149" 
auth = HTTPBasicAuth(username, password)

headers = {'Authorization':"Basic Y2xpZmZlcm5lc3Qud2FjaGl1cmlAc29mdHdhcmVhZy5jb206bnVxZXBhNXA="}


# Type can be cansMeasurement, plasticMeasurement, fillLevel1, fillLevel2 etc
def create_measurement(measurement_type, value, unit):
    url = base_url +"/measurement/measurements"
    iso_time = datetime.datetime.utcfromtimestamp(time.time()).isoformat()
    measurement_data = {
        measurement_type: {
            "M": {
                "value": value,
                "unit": unit}
        },
        "time": iso_time,
        "source": {
            "id": device_id},
        "type": measurement_type
    }
    response = requests.post(url, json=measurement_data, auth=auth)
    print(response.status_code)


# Events types could be things such as a session started and session ended
def create_event(event_type, text):
    url = base_url + "/event/events"
    iso_time = datetime.datetime.utcfromtimestamp(time.time()).isoformat()

    event_data = {

        "source": {
            "id": device_id},
        "type": event_type,
        "text": text,
        "time": iso_time,
    }

    response = requests.post(url, json=event_data, auth=auth)

    print(response.status_code)


# Alarm type can be something like cans too full etc.
# Severity can only be WARNING, MINOR, MAJOR, CRITICAL

def create_alarm(alarm_type, text, severity):
    url = base_url + "/alarm/alarms"
    iso_time = datetime.datetime.utcfromtimestamp(time.time()).isoformat()

    alarm_data = {

        "source": {
            "id": device_id},
        "type": alarm_type,
        "text": text,
        "severity": severity,
        "time": iso_time,
    }

    response = requests.post(url, json=alarm_data, auth=auth)

    print(response.status_code)


#create_measurement("testMeasurement",25,"%")
#create_alarm("test_alarm","The can bin has overflown","MAJOR")
#create_event("test_event", "Zobalo has restarted")