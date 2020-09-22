"""
Schemas validating the input to API endpoints.
"""
from marshmallow import Schema, fields, validates, ValidationError
from controllers import email_registered, name_registered

class RegisterSchema(Schema):
    """
    Schema that validates the input to the register resource.
    """
    name = fields.String(required=True)
    email = fields.Email()

    @validates("email")
    def unique_email(self, email):
        """
        Validate the uniqueness requirement of the given email.
        """
        if email_registered(email):
            raise ValidationError("Email already registered")


    @validates("name")
    def unique_name(self, name):
        """
        Validate the uniqueness requirement of the given name.
        """
        if name_registered(name):
            raise ValidationError("name already registered")
