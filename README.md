# hoops-bot
HoopsBot is a Discord bot that brings live NBA scores and AI-powered game summaries right into your server.

✨ Features

🔢 Live Scores: Get real-time NBA game scores using the official NBA API

👤 Player Info: (placeholder) query player stats — expansion coming soon

🤖 AI Summaries: Fun, fan-style game recaps powered by OpenAI (if API key is set)

💬 Simple Commands:

!score Lakers → current score for the Lakers

!summary Warriors → hype update for the Warriors game

!player LeBron James → player info (placeholder for now)

🚀 Getting Started
1. Clone the Repo:
    git clone https://github.com/yourusername/hoops-bot.git
    cd hoops-bot

2. Set Up a Virtual Environment
    python3 -m venv .venv
    source .venv/bin/activate

3. Install Dependencies
    pip install -r requirements.txt

4. Configure Environment

Copy the example file and fill in your keys:

    cp .env.example .env

Edit .env:
    DISCORD_TOKEN=your_discord_token_here
    OPENAI_API_KEY=sk-your_openai_api_key_here
    BOT_PREFIX=!

5. Run the Bot

    python bot.py



⚙️ Setup in Discord

1. Go to the Discord Developer Portal
2. Create an application → Add Bot
3. Copy the bot token into .env
4. Under OAuth2 → URL Generator:
Scopes → bot
Bot Permissions → Read/Send Messages
5. Invite the bot to your server with the generated link

📂 Project Structure:
.
├── bot.py          # main bot logic
├── nba_data.py     # fetches NBA data
├── summarizer.py   # AI hype summaries
├── requirements.txt
├── .env.example    # template for environment variables
└── README.md

🛠️ Roadmap

✅ Live scores

✅ AI summaries

🚧 Player stats integration

🚧 Game highlights / auto-updates

🚧 Deployment with Docker/Cloud