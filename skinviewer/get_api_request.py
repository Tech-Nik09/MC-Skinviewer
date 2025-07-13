import requests
import json
import base64


def get_player_information(user_input):
    base_url = "https://api.minecraftservices.com/minecraft/profile/lookup/name/"
    response = requests.get(base_url + user_input)
    data = response.json()
    return data

def get_skin_data(uuid):
    base_url = "https://sessionserver.mojang.com/session/minecraft/profile/"
    response = requests.get(base_url + uuid)
    data = response.json()

    value_encoded = data["properties"][0]["value"]
    value_decoded = base64.b64decode(value_encoded)

    skin_url = json.loads(value_decoded)["textures"]["SKIN"]["url"]
    response = requests.get(skin_url)
    skin_binary_data = response.content 
    return skin_binary_data

def get_image_url(uuid, yaw, shadow, cape, helmet, overlay):
    base_url = "https://vzge.me/full"
    size = 832
    
    image_url = (f"{base_url}/{size}/{uuid}.png?y={yaw - 20}&no=ears,")
    if shadow == False:
        image_url += "shadow,"
    if cape == False:
        image_url += "cape,"
    if helmet == False:
        image_url += "helmet,"
    if overlay == False:
        image_url += "overlay,"
    
    return image_url
