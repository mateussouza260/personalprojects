import requests
from _datetime import datetime as dt

USERNAME = "mateus"
TOKEN = "zxc123zxc123zxc123"
GRAPH_ID = "graph1"
TODAY_DATE = dt.now().strftime("%Y%m%d")

# Creating new user ---------------------------------------------------------------
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Creating new graph ---------------------------------------------------------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Coding tracker",
    "unit": "minutes",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# Post method ---------------------------------------------------------------
pixela_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

post_params = {
    "date": TODAY_DATE,
    "quantity": "113"
}

# response = requests.post(url=pixela_creation_endpoint, json=post_params, headers=headers)
# print(response.text)


# Update method ---------------------------------------------------------------
pixela_update_endpoint = f"{pixela_creation_endpoint}/{TODAY_DATE}"

update_params = {
    "quantity": "122",
}

# response = requests.put(url=pixela_update_endpoint, json=update_params, headers=headers)
# print(response.text)

# Delete method ---------------------------------------------------------------
response = requests.delete(url=pixela_update_endpoint, headers=headers)
print(response.text)
