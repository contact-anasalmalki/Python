player1 = {
    "username": "alpha_99",
    "score": 85,
    "favorite_game": "chess",
    "achievements": ["first_win", "speedrun"],
}
player2 = {
    "username": "shadow_coder",
    "score": 42,
    "favorite_game": "portal",
    "achievements": ["first_win"],
}
player3 = {
    "username": "speedy_01",
    "score": 65,
    "favorite_game": "chess",
    "achievements": ["marathon", "speedrun"],
}
users = [player1, player2, player3]
player4 = {
    "username": "neon_rider",
    "score": 12,
    "favorite_game": "tetris",
    "achievements": [],
}
users.append(player4)
player2["score"] = 55  # this also works users[1]["score"] = 55
for user in users:
    player_name = user["username"]
    print(f"username: {player_name.title()}")
    if user["score"] >= 80:
        print(f"Ranks is Elite")
    elif 50 <= user["score"] <= 79:
        print(f"Ranks is Veteran")
    else:
        print(f"Ranks is Rookie")
    print(f"Player score is: {user["score"]}")

    # if len(user["achievements"]) != 0:
    #   print(f"\t Player Achievments: {user["achievements"]} ")
    # else:
    #   print(f"\t No achievments unlocked yet")

    if user["achievements"]:
        # this is (truthy/falsy) it will only start looping if list have items
        for achievement in user["achievements"]:
            print(f"\t Player Achievments: {achievement} ")
    else:
        print(f"\t No achievments unlocked yet")

    # for game in user["favorite_game"]:
    # all_games.append(game)
    # this will print letters ['c', 'h', 'e', 's']
unique_games = set([user["favorite_game"] for user in users])
print(f"Unique games played on the platform: {unique_games}")
search_username = "neon_rider"
usernames = [user["username"] for user in users]
if search_username in usernames:
    print("Account found.")
else:
    print("Account not found.")
