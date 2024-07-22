import requests
from datetime import datetime

# Fetch Chess.com stats
headers = {
    'User-Agent': 'contact matej.popovski@gmail.com if there is a problem!'
}
response = requests.get("https://api.chess.com/pub/player/MatejPopovski/stats", headers=headers)

# Check if the request was successful
if response.status_code == 200:
    stats = response.json()
else:
    print("Failed to fetch stats")
    stats = None

# Format stats in Markdown
def format_stats(stats):
    if not stats:
        return "Unable to fetch Chess.com stats."

    rapid = stats.get("chess_rapid", {})
    blitz = stats.get("chess_blitz", {})
    bullet = stats.get("chess_bullet", {})

    last_updated = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    markdown = f"""
## ♞ Live Chess.com Stats for MatejPopovski

### Rapid
- **Rating:** {rapid.get("last", {}).get("rating", "N/A")}
- **Wins:** {rapid.get("record", {}).get("win", "N/A")}
- **Losses:** {rapid.get("record", {}).get("loss", "N/A")}
- **Draws:** {rapid.get("record", {}).get("draw", "N/A")}

### Blitz
- **Rating:** {blitz.get("last", {}).get("rating", "N/A")}
- **Wins:** {blitz.get("record", {}).get("win", "N/A")}
- **Losses:** {blitz.get("record", {}).get("loss", "N/A")}
- **Draws:** {blitz.get("record", {}).get("draw", "N/A")}

### Bullet
- **Rating:** {bullet.get("last", {}).get("rating", "N/A")}
- **Wins:** {bullet.get("record", {}).get("win", "N/A")}
- **Losses:** {bullet.get("record", {}).get("loss", "N/A")}
- **Draws:** {bullet.get("record", {}).get("draw", "N/A")}

_Last updated: {last_updated}_
"""
    return markdown

# Get formatted stats
formatted_stats = format_stats(stats)

# Read the existing README content
with open("README.md", "r") as file:
    readme_content = file.read()

# Define the start and end markers for the stats section
start_marker = "## ♞ Live Chess.com Stats for MatejPopovski"
end_marker = "_Last updated:"

# Check if the markers exist in the readme
if start_marker in readme_content and end_marker in readme_content:
    before_stats = readme_content.split(start_marker)[0]
    after_stats = readme_content.split(end_marker)[-1].split("\n", 1)[-1]
    updated_readme = before_stats + formatted_stats + after_stats
else:
    updated_readme = readme_content + "\n" + formatted_stats

# Write the updated README content
with open("README.md", "w") as file:
    file.write(updated_readme)

print("GitHub README updated successfully!")
