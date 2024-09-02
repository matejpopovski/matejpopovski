import requests
from datetime import datetime

# Fetch Chess.com stats
headers = {
    'User-Agent': 'contact matej.popovski@gmail.com if there is a problem!'
}
chess_response = requests.get("https://api.chess.com/pub/player/MatejPopovski/stats", headers=headers)

# Check if the Chess.com request was successful
if chess_response.status_code == 200:
    chess_stats = chess_response.json()
else:
    print("Failed to fetch Chess.com stats")
    chess_stats = None

# Fetch LeetCode stats
leetcode_response = requests.get("https://leetcode-stats-api.herokuapp.com/matejpopovski")

# Check if the LeetCode request was successful
if leetcode_response.status_code == 200:
    leetcode_stats = leetcode_response.json()
    total_solved = leetcode_stats.get("totalSolved", "N/A")
    world_ranking = leetcode_stats.get("ranking", "N/A")
else:
    print("Failed to fetch LeetCode stats")
    total_solved = "N/A"
    world_ranking = "N/A"

# Format stats in Markdown
def format_stats(chess_stats):
    if not chess_stats:
        return "Unable to fetch Chess.com stats."

    rapid = chess_stats.get("chess_rapid", {})
    blitz = chess_stats.get("chess_blitz", {})
    bullet = chess_stats.get("chess_bullet", {})

    last_updated = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    markdown = f"""
<!-- START LEETCODE STATS -->
## <img src="https://upload.wikimedia.org/wikipedia/commons/1/19/LeetCode_logo_black.png" alt="LeetCode" width="20" height="25" style="vertical-align: middle; margin-bottom: -10px;"/>  Live LeetCode Stats for MatejPopovski

- **Total Problems Solved:** {total_solved}
- **World Ranking:** {world_ranking}
<!-- END LEETCODE STATS -->

<!-- START CHESS.COM STATS -->
## <img src="https://images.chesscomfiles.com/uploads/v1/images_users/tiny_mce/PedroPinhata/phpkXK09k.png" width="17" height="22" style="vertical-align: middle; margin-bottom: -10px;"/> Live Chess.com Stats for MatejPopovski

| Game Mode | Rating | Wins | Losses | Draws |
|-----------|--------|------|--------|-------|
| **Rapid** | {rapid.get("last", {}).get("rating", "N/A")} | {rapid.get("record", {}).get("win", "N/A")} | {rapid.get("record", {}).get("loss", "N/A")} | {rapid.get("record", {}).get("draw", "N/A")} |
| **Blitz** | {blitz.get("last", {}).get("rating", "N/A")} | {blitz.get("record", {}).get("win", "N/A")} | {blitz.get("record", {}).get("loss", "N/A")} | {blitz.get("record", {}).get("draw", "N/A")} |
| **Bullet** | {bullet.get("last", {}).get("rating", "N/A")} | {bullet.get("record", {}).get("win", "N/A")} | {bullet.get("record", {}).get("loss", "N/A")} | {bullet.get("record", {}).get("draw", "N/A")} |

_Last updated: {last_updated}_
<!-- END CHESS.COM STATS -->
"""
    return markdown

# Get formatted stats
formatted_stats = format_stats(chess_stats)

# Read the existing README content
with open("README.md", "r") as file:
    readme_content = file.read()

# Define the start and end markers for the stats section
start_marker = "<!-- START LEETCODE STATS -->"
end_marker = "<!-- END CHESS.COM STATS -->"

# Find the start and end indices for replacement
start_index = readme_content.find(start_marker)
end_index = readme_content.find(end_marker)

# Replace or append stats section
if start_index != -1 and end_index != -1:
    # Replace existing section
    updated_readme = (readme_content[:start_index] +
                      formatted_stats +
                      readme_content[end_index + len(end_marker):])
else:
    # Append if markers are not found
    updated_readme = readme_content + "\n" + formatted_stats

# Write the updated README content
with open("README.md", "w") as file:
    file.write(updated_readme)

print("GitHub README updated successfully!")
