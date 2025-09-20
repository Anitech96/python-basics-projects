import random
import sys
from time import sleep

class FakeNewsGenerator:
    def __init__(self):
        self.subjects = [
            "Shah Rukh Khan", "Virat Kohli", "A Mumbai Cat", "A Group of Monkeys",
            "A Pune Pigeon", "A Gang of Goats", "Arjun Mehta", "Neha Reddy",
            "A Chennai Crow", "A Band of Elephants", "A Kolkata Sparrow",
            "A Pack of Hyenas", "A Delhi Lizard", "A Team of Engineers",
            "Ravi Deshmukh", "A Mumbai Crow", "A Herd of Cows", "A Swarm of Bees",
            "A Group of Fishermen", "A Jaipur Peacock",
        ]

        self.actions = [
            "launches", "cancels", "dances with", "eats", "declares war on",
            "orders", "celebrates", "chases", "ignores", "whispers to",
            "paints", "builds", "steals from", "investigates", "hides from",
            "talks about", "teaches", "sings to", "crashes", "runs away from",
            "throws", "repairs", "bumps into", "competes with", "meditates with",
            "complains about", "jumps over", "prepares", "searches for", "introduces",
            "imitates", "organizes", "catches", "ignites", "explores", "debates with",
            "rescues", "misplaces", "pranks"
        ]

        self.places = [
            "at Red Fort", "in Mumbai Local Train", "a plate of samosa",
            "inside parliament", "at Ganga Ghat", "during IPL Match",
            "at India Gate", "on top of Gateway of India", "in a crowded market",
            "at Taj Mahal", "inside a cricket stadium", "at a roadside tea stall",
            "in a Bollywood movie set", "during Ganpati Festival", "at Marine Drive",
            "inside a chaiwala's shop", "at Juhu Beach", "on a rickshaw ride",
            "during Holi celebrations", "in a dhaba kitchen", "at Charminar",
            "inside a snake charmer's basket", "on top of a mango tree", "in a crowded wedding hall",
            "at a political rally", "during monsoon rain", "inside an auto-rickshaw",
            "at a street food stall", "in a noisy train station", "at a roadside barber shop",
            "during Diwali fireworks", "in a temple courtyard", "at a college canteen",
            "inside a movie theater", "on the Mumbai-Pune Expressway", "during a yoga session in the park",
            "at a local fair", "in a small village market", "on the terrace of a building",
            "inside a noisy bazaar"
        ]
        
        # ANSI color codes
        self.colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
            'white': '\033[97m',
            'reset': '\033[0m'
        }
    
    def generate_headline(self):
        """Generate a random fake news headline"""
        subject = random.choice(self.subjects)
        action = random.choice(self.actions)
        place = random.choice(self.places)
        
        return f"{self.colors['red']}BREAKING NEWS: {self.colors['reset']}{subject} {action} {place}"

    def print_intro(self):
        """Print the introduction banner"""
        print(f"{self.colors['cyan']}{'='*60}")
        print("       FAKE NEWS HEADLINE GENERATOR")
        print("           INDIAN EDITION")
        print(f"{'='*60}{self.colors['reset']}")
        print(f"{self.colors['yellow']}Generate hilarious and absurd news headlines!")
        print(f"Perfect for laughs, creative writing, or social media content.{self.colors['reset']}")
        print()

    def print_outro(self):
        """Print the farewell message"""
        print(f"\n{self.colors['green']}Thanks for using the Fake News Headline Generator!")
        print("Hope you had a good laugh! 😄")
        print(f"Share your favorite headlines with friends!{self.colors['reset']}")

    def run(self):
        """Run the main generator loop"""
        self.print_intro()
        
        while True:
            # Generate and display headline
            headline = self.generate_headline()
            print("\n" + headline)
            
            # Ask if user wants another headline
            while True:
                try:
                    user_input = input(f"\n{self.colors['blue']}Generate another headline? (yes/no): {self.colors['reset']}").strip().lower()
                    if user_input in ['yes', 'y', 'no', 'n']:
                        break
                    else:
                        print(f"{self.colors['yellow']}Please enter 'yes' or 'no'.{self.colors['reset']}")
                except KeyboardInterrupt:
                    print("\n\nExiting...")
                    self.print_outro()
                    sys.exit(0)
            
            if user_input in ['no', 'n']:
                break
                
            # Add a little delay for effect
            sleep(0.5)
        
        self.print_outro()

if __name__ == "__main__":
    try:
        generator = FakeNewsGenerator()
        generator.run()
    except KeyboardInterrupt:
        print(f"\n{generator.colors['red']}Program interrupted. Exiting...{generator.colors['reset']}")
        sys.exit(0)