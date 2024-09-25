import random
import matplotlib.pyplot as plt

# Soccer field dimensions in meters (standard: 105m x 68m)
FIELD_LENGTH = 105
FIELD_WIDTH = 68

class Shot:
    def __init__(self, player, x, y, on_target):
        self.player = player
        self.x = x  # x-coordinate of the shot
        self.y = y  # y-coordinate of the shot
        self.on_target = on_target  # Whether the shot was on target (goal)

    def __str__(self):
        return f"Player: {self.player}, Position: ({self.x}, {self.y}), On Target: {self.on_target}"

class Player:
    def __init__(self, name):
        self.name = name
        self.shots = []  # List to track all shots taken

    def take_shot(self):
        # Randomize shot position (you can customize this logic)
        x = random.uniform(0, FIELD_LENGTH)
        y = random.uniform(0, FIELD_WIDTH)
        # Randomly determine if the shot was on target
        on_target = random.choice([True, False])
        shot = Shot(self.name, x, y, on_target)
        self.shots.append(shot)

    def display_shots(self):
        for shot in self.shots:
            print(shot)

    def plot_shots(self):
        x_on_target = [shot.x for shot in self.shots if shot.on_target]
        y_on_target = [shot.y for shot in self.shots if shot.on_target]
        x_off_target = [shot.x for shot in self.shots if not shot.on_target]
        y_off_target = [shot.y for shot in self.shots if not shot.on_target]
        
        plt.figure(figsize=(10, 6))
        plt.plot([0, FIELD_LENGTH], [FIELD_WIDTH/2, FIELD_WIDTH/2], color="black")  # Halfway line
        plt.plot([0, FIELD_LENGTH], [0, 0], color="black")  # Bottom of field
        plt.plot([0, FIELD_LENGTH], [FIELD_WIDTH, FIELD_WIDTH], color="black")  # Top of field
        plt.plot([0, 0], [0, FIELD_WIDTH], color="black")  # Left side
        plt.plot([FIELD_LENGTH, FIELD_LENGTH], [0, FIELD_WIDTH], color="black")  # Right side
        
        plt.scatter(x_on_target, y_on_target, color='green', label="On Target")
        plt.scatter(x_off_target, y_off_target, color='red', label="Off Target")
        plt.title(f"Shots taken by {self.name}")
        plt.xlabel("Field Length (m)")
        plt.ylabel("Field Width (m)")
        plt.legend()
        plt.show()

# Example usage:
player1 = Player("John Doe")

# Simulate the player taking 10 shots
for _ in range(10):
    player1.take_shot()

# Display shot details
player1.display_shots()

# Plot the shots on the field
player1.plot_shots()
