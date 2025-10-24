from actions.base import Action

class FarewellAction(Action):
    def run(self, **kwargs):
        self.say("Goodbye! Have a great day!")
