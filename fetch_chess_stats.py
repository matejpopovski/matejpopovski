import requests

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

    markdown = f"""
## ♞ Live Chess.com Stats for MatejPopovski:

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
"""
    return markdown

# Get formatted stats
formatted_stats = format_stats(stats)

# Read the existing README content
with open("README.md", "r") as file:
    readme_content = file.read()

# Insert formatted stats (customize the placement)
updated_readme = readme_content.split("## Chess.com Stats")[0] + formatted_stats

# Write the updated README content
with open("README.md", "w") as file:
    file.write(updated_readme)

print("GitHub README updated successfully!")
