class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        
    def top_scorers_by_nationality(self, nationality):
        data = self.reader.get_players()
        filter_result = filter(lambda player:player.nationality == nationality, data)

        return sorted(filter_result, key=lambda player:player.total, reverse=True)