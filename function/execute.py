import requests


def lambda_handler(event, context):
    requests.get("www.google.com")
    return "cool cool"
