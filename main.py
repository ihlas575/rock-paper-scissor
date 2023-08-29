import random
from message import Result

items = ["rock ✊", "paper ✋", "scissor ✌️"]
chances = 0
scores = 0
bot_score = 0

while chances < 3:
    item = random.choice(items)
    guess = input('Guess ["Rock", "Paper", "Scissor"]: ').lower()

    # Make a result object
    result = Result()

    # Rock Physics
    if item == "rock ✊" and guess == "paper":
        scores += 1
        chances += 1
        result.won(item, scores, bot_score)

    elif item == "rock ✊" and guess == "scissor":
        bot_score += 1
        chances += 1
        result.lose(item, scores, bot_score)

    elif item == "rock ✊" and guess == "rock":
        chances += 1
        result.tie(item, scores, bot_score)

    # Paper Physics
    elif item == "paper ✋" and guess == "scissor":
        scores += 1
        chances += 1
        result.won(item, scores, bot_score)

    elif item == "paper ✋" and guess == "rock":
        bot_score += 1
        chances += 1
        result.lose(item, scores, bot_score)

    elif item == "paper ✋" and guess == "paper":
        chances += 1
        result.tie(item, scores, bot_score)

    # Scissor Physics
    elif item == "scissor ✌️" and guess == "rock":
        scores += 1
        chances += 1
        result.won(item, scores, bot_score)

    elif item == "scissor ✌️" and guess == "paper":
        bot_score += 1
        chances += 1
        result.lose(item, scores, bot_score)

    elif item == "scissor ✌️" and guess == "scissor":
        chances += 1
        result.tie(item, scores, bot_score)

    # When clients make mistakes this will appear
    else:
        print("Invalid Value.")

else:
    if bot_score < scores:
        print(f"\nWinner Winner Chicken Dinner! 🐔 \nScores = {scores}:{bot_score}")

    elif bot_score > scores:
        print(f"\nGame Over! \nYou Lost! \nScores = {scores}:{bot_score}")

    else:
        print(f"It's a Tie Match...")
