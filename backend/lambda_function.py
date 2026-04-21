import json
import base64
from parser import extract_text
from ats_scoring import calculate_score

def lambda_handler(event, context):

    body = json.loads(event['body'])
    file_content = base64.b64decode(body['file'])

    text = extract_text(file_content)
    result = calculate_score(text)

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(result)
    }
