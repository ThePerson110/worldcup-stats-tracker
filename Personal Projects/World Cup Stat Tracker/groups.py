from api import get

def get_all_groups():
    return get("/standings")

def get_group(group_letter):
    groups = get_all_groups()
    for g in groups:
        if g["group"].lower() == group_letter.lower():
            return g
    return None
