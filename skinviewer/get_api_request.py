import requests
import json
import base64

def get_uuid(playername):
    base_url = "https://api.minecraftservices.com/minecraft/profile/lookup/name/"
    response = requests.get(base_url + playername)
    data = response.json()
    if "id" in data:
        uuid = data["id"]
        return uuid
    else:
        print(f"[WARN] No player with name '{playername}' found.")

def get_skin_url(uuid):
    base_url = "https://sessionserver.mojang.com/session/minecraft/profile/"
    response = requests.get(base_url + uuid)
    data = response.json()
    value_encoded = data["properties"][0]["value"]
    value_decoded = base64.b64decode(value_encoded)
    skin_url = json.loads(value_decoded)["textures"]["SKIN"]["url"]
    return skin_url

def get_image_url(uuid = "33e10a68a14e49acafa84d67399a4bff", yaw = 0, shadow = True, cape = True, helmet = True, overlay = True):
    base_url = "https://vzge.me/full"
    size = 832
    
    image_url = (f"{base_url}/{size}/{uuid}?y={yaw}&no=ears,")
    
    if shadow == False:
        image_url += "shadow,"
    if cape == False:
        image_url += "cape,"
    if helmet == False:
        image_url += "helmet,"
    if overlay == False:
        image_url += "overlay,"
    
    return image_url