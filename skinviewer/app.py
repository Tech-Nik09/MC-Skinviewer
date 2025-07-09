import get_mojangapi_request

playername = input("Enter a playername to search for: ")
uuid = get_mojangapi_request.get_uuid(playername)
print(uuid)