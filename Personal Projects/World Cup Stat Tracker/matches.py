from api import get

def get_all_matches():
    return get("/matches")

def get_matches_by_team(team_name):
    matches = get_all_matches()
    return [
        m for m in matches
        if team_name.lower() in m["home_team"]["name"].lower()
        or team_name.lower() in m["away_team"]["name"].lower()
    ]

def get_upcoming_matches():
    matches = get_all_matches()
    return [m for m in matches if m["status"] == "scheduled"]

def get_completed_matches():
    matches = get_all_matches()
    return [m for m in matches if m["status"] == "completed"]
