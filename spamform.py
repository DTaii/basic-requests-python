import requests
import threading
import random
def send_request():
    data = {
        "entry.1132092760": random.choice(["Ngủ", "Xem phim", "Đá bóng"]),
        "entry.214361889": random.choice(["1890", "1980"]),
        "entry.214361889 sentinel": ""
    }
    response = requests.post("https://docs.google.com/forms/u/0/d/e/1FAIpQLSeUfy9wdq2zQvuX1dTU5e0j3Ei4PUMCBSp4Vgv2uoBy7pc2Cg/formResponse", data=data)
    status = response.status_code
    if status == 200:
        print("Sent successfully")
    else:
        print("Sending failed")
arrthread = []
for i in range(10000):
	t = threading.Thread(target=send_request)
	arrthread.append(t) 
for t in arrthread:
	t.start()