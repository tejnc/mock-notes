import json

headers = {
    "Content-Type":"application/json",
    "Access-Control-Allow-Origin":"*",
    "Access-Control-Allow-Credentials": True,
}


def success_response(status_code, message, data):
    return response(data=data, success=True, message=message, status_code=status_code)


def error_response(status_code, message):
    return response(data=None, success=False, message=message, status_code=status_code)


def response(data, success, message, status_code):
    body = {"message": message, "success": success, "data": data}
    return {"statusCode": status_code, "headers": headers, "body": json.dumps(body)}
