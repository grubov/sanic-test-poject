from marshmallow import Schema, fields


class ContractSchema(Schema):
    title = fields.String(required=True)
    price = fields.Float(required=True)
    comment = fields.String()


class PaymentSchema(Schema):
    amount = fields.Float(required=True)
