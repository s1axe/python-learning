games = [
    {"name": "Rust", "hours": 600, "rating": 51},
    {"name": "CS2", "hours": 3500, "rating": 43},
    {"name": "Minecraft", "hours": 800, "rating": 3},
    {"name": "Valorant", "hours": 200, "rating": 8}
]
for game in games:
    if game["rating"] > 8:
        print(game["name"])
  