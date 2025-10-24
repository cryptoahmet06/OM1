from src.actions.base import Action
import random

class JokeAction(Action):
    jokes = [
        "Why did the robot go back to school? Because its skills were getting rusty!",
        "Why did the AI cross the road? To optimize its path!",
        "Why don't robots ever get tired? They have power-saving mode!"
    ]

    def run(self, input_data):
        joke = random.choice(self.jokes)
        self.say(joke)
        return joke
