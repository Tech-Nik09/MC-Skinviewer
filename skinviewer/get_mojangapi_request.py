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