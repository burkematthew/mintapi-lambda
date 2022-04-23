import requests


def lambda_handler(event, context):
    requests.get("http://www.google.com")
    return "cool cool"
