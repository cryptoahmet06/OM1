def greet(name: str):
    """Simple greeting action for Spot agent."""
    print(f"Hello, {name}! Welcome to OM1.")

class CustomGreetAction:
    def __init__(self):
        self.name = "custom_greet"

    def run(self, params):
        name = params.get("name", "user")
        print(f"Hello, {name}! Welcome to OM1.")