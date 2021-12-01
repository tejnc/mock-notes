from mongoengine.fields import DateTimeField, StringField
from mongoengine_goodjson import Document


class Notes(Document):
    """models for saving notes"""

    title = StringField(min_length=3)
    description = StringField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

    meta = {"collection": "notes"}
