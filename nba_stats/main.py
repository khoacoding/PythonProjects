from requests import get
from pprint import PrettyPrinter

BASE_URL = "http://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links

def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    teams = get(BASE_URL + scoreboard).json()['games']
    for team in teams:
        home_team = team['hTeam']
        visit_team = team['vTeam']
        print(f"{home_team['triCode']} {home_team['score']} - {visit_team['score']} {visit_team['triCode']} ")
        print("----------------------------")

def get_standing():
    standing = get_links()['leagueUngroupedStandings']
    teams = get(BASE_URL + standing).json()['league']['standard']['teams']
    teams.sort(key=lambda x: int(x['sortKey']['win']), reverse=True)
    for team in teams:
        team_name = team['teamSitesOnly']['teamTricode']
        win_loss = team['sortKey']
        print(f"{team_name} Win: {win_loss['win']} - Loss: {win_loss['loss']}")


def main():
    while True:
        user_view = input("What do you want to view (1 for current scoreboard, 2 for teams standing), press 'q' to quit: ")
        if user_view == "q":
            break
        if user_view == "1":
            get_scoreboard()
        elif user_view == "2":
            get_standing()
        else:
            print("Please enter 1 or 2!")

main()