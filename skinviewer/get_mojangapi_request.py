import requests

def get_uuid(playername):
    base_url = "https://api.minecraftservices.com/minecraft/profile/lookup/name/"
    response = requests.get(base_url + playername)
    data = response.json()
    if "id" in data:
        uuid = data["id"]
        return uuid
    else:
        print(f"[WARN] No player with name '{playername}' found.")

def get_player_data(uuid):
    pass
