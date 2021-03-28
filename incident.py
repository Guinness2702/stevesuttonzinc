import json,sys, datetime

class ValidationException(Exception):
    """Raised when input field is invalid"""
    pass

def get(event, context):
    body = {
        "message": "Get received, hooray!",
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def post(event, context):

    try:
        request_body = event['body']
        body_json = json.loads(request_body)

        if "location" not in body_json:
            raise ValidationException("'location' missing from input request")

        if "category" not in body_json:
            raise ValidationException("'category' missing from input request")

        category = body_json['category']

        if not isinstance(category, int):
            raise ValidationException("'category' must be an int")

        # Note: Checking for null is not part of the spec, but we need to do it, so let's handle the same way
        if "incidentDate" not in body_json:
            raise ValidationException("'incidentDate' missing from input request")

        try:
            incident_date = datetime.datetime.strptime(body_json['incidentDate'], "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValidationException("'incidentDate' is not correctly formatted; use 'YYYY-MM-DD HH-MM-SS'")

        if "People" in body_json:
            people = body_json['People']

            allowed_keys = ['staff', 'witness', 'offender']

            for key, value in people.items():
                if key not in allowed_keys:
                    raise ValidationException("Unexpected type '" + key + "' found in 'People'")

        body = {
            "message": "Post received!",
            "input": event
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body),
        }
    except ValidationException as e:
        message = {}
        message['validationException'] = str(e)

        response = {
            "statusCode": 400,
            "body": json.dumps(message),
        }
    except Exception as e:
        message = {}
        message['exception'] = str(e)

        response = {
            "statusCode": 200,
            "body": json.dumps(message),
        }

    return response
