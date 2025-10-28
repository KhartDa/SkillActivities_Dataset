from dotenv import load_dotenv
import os, requests,json

load_dotenv()
get_point = os.getenv("XANO_GET")


r = requests.get(get_point).json()


# print(json.dumps(r))
for item in r:
    if not item == "Verify_Email":
        # print(item["First_Name"],item["Last_Name"])
        print(json.dumps(item, indent=4))
    