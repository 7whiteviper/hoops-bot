from nba_api.live.nba.endpoints import scoreboard
import time

# Cache to avoid calling the NBA API too often
_CACHE = {"ts": 0, "data": None}
_CACHE_TTL = 10  # cache for 10 seconds

def _get_raw_scoreboard():
    """
    Fetch today's NBA scoreboard with caching.
    Returns: list of game dictionaries.
    """
    now = time.time()
    if _CACHE["data"] and now - _CACHE["ts"] < _CACHE_TTL:
        return _CACHE["data"]

    sb = scoreboard.ScoreBoard()
    games = sb.games.get_dict()
    _CACHE["data"] = games
    _CACHE["ts"] = now
    return games

def find_game_score(team_name: str) -> str:
    """
    Find the current score for the given team.
    """
    games = _get_raw_scoreboard()
    team_lower = team_name.lower()

    for game in games:
        home = game.get("homeTeam", {})
        away = game.get("awayTeam", {})
        if team_lower in home.get("teamName", "").lower() or team_lower in away.get("teamName", "").lower():
            home_name = home.get("teamName", "Home")
            away_name = away.get("teamName", "Away")
            home_score = home.get("score", "0")
            away_score = away.get("score", "0")
            period = game.get("period", {}).get("current", "N/A")
            return f"{away_name} {away_score} - {home_name} {home_score} (Period: {period})"

    return f"No live game found for '{team_name}'."

def find_player_stats(player_name: str) -> str:
    """
    Placeholder for individual player stats.
    Later we’ll hook into box score endpoints.
    """
    return f"Stats for {player_name} coming soon!"

