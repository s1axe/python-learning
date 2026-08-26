game = {
    "name": "Rust",
    "hours": 600,
    "rating": 8,
    "genre": "survival",
    "year": 2018
}

for key, value in game.items():
    print(key, value)

print()

for key, value in game.items():
    if key == "hours" or key == "rating":
        print(key, value)