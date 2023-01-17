import json
import os
import mercadopago


def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["YOUR_ACCESS_TOKEN"])
    
    # TODO implement
    payment_data = {
        "transaction_amount": float(event["transaction_amount"]),
        "token": event["token"],
        "installments": int(event["installments"]),
        "payment_method_id": event["payment_method_id"],
        "issuer_id": event["issuer_id"],
        "payer": {
            "email": event["payer"]["email"],
            "identification": {
                "type": event["payer"]["identification"]["type"], 
                "number": event["payer"]["identification"]["number"]
            }
        }
    }
    
    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]
    
    return {
        "statusCode": 200,
        "body": payment,
    }