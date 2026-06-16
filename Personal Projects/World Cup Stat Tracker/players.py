from api import get

def get_all_players():
    return get("/players")

def get_player_by_id(player_id):
    return get(f"/players/{player_id}")

def search_players(name):
    players = get_all_players()
    return [p for p in players if name.lower() in p["name"].lower()]
