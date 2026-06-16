from players import get_all_players, search_players
from matches import get_all_matches, get_matches_by_team
from groups import get_all_groups, get_group

def main():
    while True:
        print("\nWorld Cup 2026 Stats Tracker")
        print("1. List all players")
        print("2. Search for a player")
        print("3. List all matches")
        print("4. Search matches by team")
        print("5. View all groups")
        print("6. View a specific group")
        print("0. Exit")

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

        elif choice == "3":
            matches = get_all_matches()
            for m in matches:
                print(f"{m['home_team']['name']} vs {m['away_team']['name']} - {m['status']}")

        elif choice == "4":
            team = input("Enter team name: ")
            results = get_matches_by_team(team)
            for m in results:
                print(f"{m['home_team']['name']} vs {m['away_team']['name']} - {m['status']}")

        elif choice == "5":
            groups = get_all_groups()
            for g in groups:
                print(f"\nGroup {g['group']}")
                for team in g["teams"]:
                    print(f"  {team['name']} - {team['points']} pts")

        elif choice == "6":
            letter = input("Enter group letter (A-H): ")
            g = get_group(letter)
            if g:
                print(f"\nGroup {g['group']}")
                for team in g["teams"]:
                    print(f"  {team['name']} - {team['points']} pts")
            else:
                print("Group not found")

        elif choice == "0":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

