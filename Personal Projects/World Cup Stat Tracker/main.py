from players import get_all_players, search_players

def main():
    print("World Cup 2026 Stats Tracker")
    print("1. List all players")
    print("2. Search for a player")
    choice = input("Choose an option: ")

    if choice == "1":
        players = get_all_players()
        for p in players:
            print(f"{p['name']} - {p['position']} - {p['team']}")
    elif choice == "2":
        name = input("Enter player name: ")
        results = search_players(name)
        for p in results:
            print(f"{p['name']} - {p['position']} - {p['team']}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
