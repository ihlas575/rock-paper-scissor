class Result:
    def won(self, item, scores, bot_score):
        print(f"\n{item.title()} \n'You Won!' \n{scores}:{bot_score} \n")

    def lose(self, item, scores, bot_score):
        print(f"\n{item.title()} \n'You Lost!' \n{scores}:{bot_score} \n")

    def tie(self, item, scores, bot_score):
        print(f"\n{item.title()} \n'It's a Tie' \n{scores}:{bot_score} \n")

