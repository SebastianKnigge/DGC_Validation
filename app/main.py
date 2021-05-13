#import from src directory
import sys
sys.path.insert(1, './app/src')

from fastapi import FastAPI

from QR_vienna import qr_validation_vienna
from QR_austria import qr_validation_austria
from URL_Identification import URL
from audittrail import audittrail_creation
from SQLite import verifier

# use mangum package for deployment
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "The service is up and running"}

@app.get("/verification/")
async def qr_validation(qr_url: str = "The QR Code you want to validate", audit_trail: bool = True,
                        apikey: str = "Your personal API key"):

    #The provided apikey equals the internal verfiy variable
    verify = apikey

    #Our verifier return a tuple with the apikey verification result in the first slot
    apikey_verification = verifier(verify)

    #We have to check if the qr_url is containing querry arguments e.g. & signs, if so, we have to replace them with %26
    if apikey_verification[0] != True:
        return {"message": "The API key validation failed"}

    URL_validation_position = URL(qr_url)

    #The API parameter equals our internal ID
    id = qr_url

    if URL_validation_position == 0:
        validation_result = qr_validation_austria(id)
        #return {"message": "URL_validation_position 0"}

    # The ID will be handed over to the QR code validation function and the output is our validation result
    if URL_validation_position == 1:
        validation_result = qr_validation_vienna(id)

    if URL_validation_position != 0 and URL_validation_position != 1:
        return {"message": "Our service is not providing the provided QR Code so far"}


    #The audit trail will only be created if the querry paramenter "audit_trail" is true (default value)
    if audit_trail == True:

        # The validation result will now used as our audit trail input
        audittrail_input = validation_result

        # The input will be handed over to the audittrail creation function
        audittrail_creation(audittrail_input, apikey_verification)

    #The return for the user is the audittrail input
    return {validation_result}


# define handler
handler = Mangum(app)