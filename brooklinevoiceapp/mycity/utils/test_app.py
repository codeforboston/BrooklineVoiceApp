from lambda_function import lambda_handler
import json
import pathlib

filename = pathlib.Path(__file__).parent / 'test_objects.json'
with open(filename) as f:
    event = json.loads(f.read())
    lambda_handler(event, event['context'])
