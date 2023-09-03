import requests

url = 'https://api.unionavatars.com/login'

headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'username': 'user@example.com',
    'password': 'string'
}

response = requests.post(url, headers=headers, data=data )

{
    "access_token": "<YOUR_TOKEN>",
    "token_type": "bearer"
}

{'Authorization': 'Bearer <ACCESS_TOKEN>'}

{'Authorization': '<TOKEN_TYPE> <ACCESS_TOKEN>'}

import requests

url = 'https://api.unionavatars.com/bodies'

headers = {
  'Authorization': 'Bearer <ACCESS_TOKEN>',
  'Content-Type': 'application/json'
}


response = requests.get(url, headers=headers)

import requests

url = 'https://api.unionavatars.com/validation/head'

headers = {
  'Authorization': 'Bearer <ACCESS_TOKEN>',
  'Content-Type': 'application/json'
}

data = {
    'img': '<IMAGE_BASE64_STRING>'
  }

response = requests.post(url, headers=headers, data=data)


import base64

with open('/path/to/your/selfie', 'rb') as img:
    encoded_string = base64.b64encode(img.read()).decode('utf-8')

    print(encoded_string)


import requests

url = 'https://api.unionavatars.com/heads'

headers = {
  'Authorization': 'Bearer <ACCESS_TOKEN>',
  'Content-Type': 'application/json'
}
2
data = {
    'name': 'My first head',
    'selfie_img': '<IMAGE_BASE64_STRING>'
  }

response = requests.post(url, headers=headers, data=data)


{
  "name": "<YASMINS_NEW_AVATAR_SEPT>",
  "head_id": "<HEAD_UUID>",
  "body_id": "<BODY_UUID>",
  "output_format": "fbx | glb"
}

import requests

url = 'https://api.unionavatars.com/avatars'

headers = {
  'Authorization': 'Bearer <ACCESS_TOKEN>',
  'Content-Type': 'application/json'
}

data = {
    'name': '<YOUR_AMAZING_AVATAR_NAME>',
    'img': '<IMAGE_BASE64_STRING>',
    'body': '<BODY_UUID>',
    'output_format': 'fbx | glb'
  }

response = requests.post(url, headers=headers, data=data)

import requests

url = 'https://api.unionavatars.com/avatars/last'

headers = {
  'Authorization': 'Bearer <ACCESS_TOKEN>',
  'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)


