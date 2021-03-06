import requests
from requests.auth import HTTPBasicAuth
import json


url = "http://127.0.0.1:5000/api/v1/"

# data = [[14.34, 1.68, 2.7, 25.0, 98.0, 2.8, 1.31, 0.53, 2.7, 13.0, 0.57, 1.96, 660.0]]
# data_json = json.dumps(data)

# username = "erdemsirel"
# password = "123"

# headers = {"content-type": "application/json",
# "Accept-Charset": "UTF-8", 
# }
# r = requests.get(
#     url + "test",
#     data=data_json,
#     params={"name": "Erdem", "surname": "Sirel"},
#     auth=(username, password),
#     headers=headers,
# )

### Create New User
user_info = {"username":"erdemsirel",
             "email": "ahmetsirel@gmail.com",
             "password": "123",
             }
user_info_json = json.dumps(user_info)
headers = {"content-type": "application/json",
"Accept-Charset": "UTF-8", 
}

r = requests.post(
    url + "user",
    headers=headers,
    data = user_info_json
)
print(r.status_code, r.message)
