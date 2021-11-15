import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")

    players = []

    for player_dict in response:
        if player_dict['nationality'] == 'FIN':

            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists'],
                player_dict['goals'] + player_dict['assists']
            )
            players.append(player)

    print("Oliot:")

    sorted_list = sorted(players, key=lambda player:player.total, reverse=True)

    for player in sorted_list:
        print(player)

if __name__ == "__main__":
    main()
