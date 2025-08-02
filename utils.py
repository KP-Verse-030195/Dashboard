# utils.py

import requests
import pandas as pd
from datetime import datetime

AUTH_URL = "https://iam.api.wayuvega.in/v1/iam/token/auth"
REPORT_URL = "https://pocas.api.wayuvega.in/v1/pocas/report/all"

USERNAME = "babyteddy"
PASSWORD = "babyteddy@123"

def get_auth_token():
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(AUTH_URL, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()['token']

def fetch_mis_report(token, from_date, to_date):
    headers = {"Authorization": token}
    params = {
        "reportName": "MIS_ALL",
        "fromDate": from_date,
        "toDate": to_date
    }
    response = requests.post(REPORT_URL, headers=headers, params=params)
    response.raise_for_status()
    # Assuming API response is CSV content
    # If it's a file download, adapt accordingly
    # Otherwise if it's JSON data, convert to DataFrame
    # Example:
    # data = response.json()
    # df = pd.DataFrame(data)
    # return df

    # if response returns file:
    with open("report.csv", "wb") as f:
        f.write(response.content)
    df = pd.read_csv("report.csv")
    return df

def format_date_for_api(date_obj):
    return date_obj.strftime("%Y-%m-%d")
