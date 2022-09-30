import requests
import json

baseUrl = "http://10.80.144."

baseText = "/OriginacionCentralizada/originacion/test"


with open("respuestas-originacion.txt", "w", encoding="utf-8") as f:
    for suffix in range(135, 147):
        for port in range(8084, 8087):
            nodeUrl = f"{baseUrl}{suffix}:{port}{baseText}"

            f.write(f"{nodeUrl}\n\n")

            response = "something went wrong"

            try:
                print("testing " + nodeUrl)
                response = requests.get(nodeUrl, timeout=1)
                f.write(f"{json.dumps(response.json())}\n\n")
            except Exception as e:
                f.write(f"{response}\n\n")
