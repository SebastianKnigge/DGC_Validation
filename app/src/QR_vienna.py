import requests
import socket
from datetime import datetime
from bs4 import BeautifulSoup


# The QR code id is the input paramenter of the function
def qr_validation_vienna(id):
    # issuing authority
    authority = "City of Vienna"

    # building the final url
    url = id

    # requesting the url
    qr_validation = requests.get(url)

    # url validation
    status_code = qr_validation.status_code

    # webserver check
    if status_code == 200:

        # parsing it in HTML
        QR_html = BeautifulSoup(qr_validation.text, "html.parser")

        # extraction of the required information based on the qr code url
        data = QR_html.find_all("p")
        first_name = data[0].text
        last_name = data[1].text
        date_of_birth = data[2].text
        test_date = data[3].text

        # adding a validation time stamp
        current_date = datetime.now()
        test_validation = current_date.strftime("%d.%m.%Y %H:%M")

        # validator identification
        validator = socket.gethostname()

        # return values
        return first_name, last_name, date_of_birth, test_date, test_validation, authority, id, validator

    # city vienna webserver is offline (does not mean that the result is not valid)
    else:
        offline = "the city vienna webserver is offline"
        return offline, offline, offline, offline, offline, offline, offline, offline