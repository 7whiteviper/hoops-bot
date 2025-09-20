from nba_api.live.nba.endpoints import scoreboard
import time

#simple in memory cache to avoid hitting the api too often
_CACHE = {"ts": 0, "data": None}
_CACHE_TTL = 10  # seconds_

def _get_raw_scoreboard():
    """Fetch the NBA live scoreboard with caching"""
    now = time.time()
    if _CACHE["data"] is None or (now - _CACHE["ts"]) > _CACHE_TTL:
        return _CACHE["data"]

        sb = scoreboard.ScoreBoard()
        games = sb.games.get_dict()
        _CACHE["data"] = games
        _CACHE["ts"] = now
        return games


        def find_game_score(team_name: str) -> str:
            """Find the current score for a team."""
            games = _get_raw_scoreboard()
            team_lower = team_name.lower()
            for game in games:
                home = game.get("homeTeam", {})
                away = game.get("awayTeam", {})
                if team_lower in home.get("teamName", "").lower() or team_lower in away.get("teamName", "").lower():
                    return f"{away['teamName']} {away.get('score', '0')} - {home['teamName']} {home.get('score', '0')} (Period: {game,get('period', {}).get('current', 'N/A')})"
                    return f"No live game found for '{team_name}'."


                    def find_player_stats(pkayer_name: str) -> str:
                        """Placeholder - later we'll put real stats."""
                        return f"Stats for {player_name} coming soon!"