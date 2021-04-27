
QR_list = ["https://qr.gv.at/v/", "https://app.wien.gv.at/validierung"]

def URL(qr_url):

    full_URL = qr_url
    URL_split = full_URL.split("?")
    URL_static = URL_split[0]
    print(URL)

    for i in range(len(QR_list)):
        if URL_static in QR_list[i]:
            position = i

    return position





