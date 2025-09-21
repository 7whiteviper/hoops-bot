import os
from openai import OpenAI
from nba_data import _get_raw_scoreboard

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def _build_prompt(team_name: str, game_snapshot: str) -> str:
    return (
        f"Write a 1-2 sentence energetic, fan-style update about the current {team_name} game. "
        f"Include the score and one highlight. Snapshot: {game_snapshot}"
    )

def summarize_game_text(team_name: str) -> str:
    games = _get_raw_scoreboard()
    game_snapshot = "No game data."

    for game in games:
        home = game.get("homeTeam", {})
        away = game.get("awayTeam", {})
        if team_name.lower() in home.get("teamName", "").lower() or team_name.lower() in away.get("teamName", "").lower():
            game_snapshot = f"{away.get('teamName')} {away.get('score')} vs {home.get('teamName')} {home.get('score')}"
            break

    if not client.api_key:
        return f"(No AI key set) Quick update: {game_snapshot}"

    prompt = _build_prompt(team_name, game_snapshot)

    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}],
        max_tokens=80,
        temperature=0.8
    )
    return resp.choices[0].message.content.strip()
