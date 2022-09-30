import requests
import json

baseUrl = "https://10.80.142."

baseText = "/SolicitudCreditoWeb/service/rest/public/test"


with open("respuestas-solicitudweb.txt", "w", encoding="utf-8") as f:
    for suffix in range(113, 122):
        for port in ["8443","8543","8643"]:
            nodeUrl = f"{baseUrl}{suffix}:{port}{baseText}"

            f.write(f"{nodeUrl}\n\n")

            response = "something went wrong"

            try:
                print("testing " + nodeUrl)
                response = requests.get(nodeUrl, timeout=1, verify = False)
                f.write(f"{json.dumps(response.json())}\n\n")
            except Exception as e:
                f.write(f"{response}\n\n")
                print(e)
