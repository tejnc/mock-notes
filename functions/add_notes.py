from datetime import datetime
from json import dump, dumps
from aws_lambda_powertools.utilities.data_classes import event_source
from aws_lambda_powertools.utilities.data_classes.api_gateway_proxy_event import APIGatewayProxyEventV2
from aws_lambda_powertools.utilities.typing.lambda_context import LambdaContext


from utils.mongo import db_config
from models.notes import Notes
from utils.response import success_response


@event_source(data_class=APIGatewayProxyEventV2)
def main(event: APIGatewayProxyEventV2, context: LambdaContext):
    body = event.json_body
    
    db_config()


    note: Notes = Notes(
        title=body["title"],
        description=body["description"],
        created_at=datetime.utcnow()
    )
    note.save()

    return success_response(status_code=200, message="Success", data=dumps(note.to_json()))