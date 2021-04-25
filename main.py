from fastapi import FastAPI
import QR_vienna

import audittrail

app = FastAPI()

password = "abcd"


@app.get("/verification/")
async def qr_validation(qr_url: str = "The QR Code you want to validate", audit_trail: bool = True,
                        apikey: str = "Your personal API key"):

    if apikey != password:
        return {"message": "The API key validation failed"}

    #The API parameter equals our internal ID
    id = qr_url
    #The ID will be handed over to the QR code validation function and the output is our validation result
    validation_result = QR_vienna.qr_validation_vienna(id)


    #The audit trail will only be created if the querry paramenter "audit_trail" is true (default value)
    if audit_trail == True:
        # The validation result will now used as our audit trail input
        audittrail_input = validation_result
        # The input will be handed over to the audittrail creation function
        audittrail.audittrail_creation(audittrail_input)


    #The return for the user is the audittrail input
    return {audittrail_input}

