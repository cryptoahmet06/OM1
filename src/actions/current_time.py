from actions.base import Action
from datetime import datetime

class CurrentTimeAction(Action):
    def run(self, **kwargs):
        now = datetime.now().strftime("%H:%M")
        self.say(f"The current time is {now}.")
