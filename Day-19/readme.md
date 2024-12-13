# Day 19: Lottery Simulation Using the `random` Module

## **Task**: Create a lottery simulation to understand the usage of the `random` module in Python.

**Description**:  
The `random` module in Python provides functions to generate random numbers or choose random items from a sequence. In today’s task, you will create a simple lottery simulation where random numbers are generated and compared to user-selected numbers.

You will:  
1. Use the `random.sample()` method to generate random lottery numbers.  
2. Allow the user to input their lottery numbers.  
3. Compare the numbers and determine the results.  
4. Enhance the task with bonus challenges like multiple players or different prize tiers.

---

## 1. Generating Random Lottery Numbers
Use the `random.sample()` method to pick unique random numbers.

```python
import random

# Generate 5 random numbers between 1 and 50
lottery_numbers = random.sample(range(1, 51), 5)
print("Today's Lottery Numbers are:", lottery_numbers)
```

## 2. User Input for Lottery Numbers
Prompt the user to enter their chosen numbers.

```python
# User enters 5 numbers
user_numbers = []
print("Enter 5 numbers between 1 and 50:")

for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    while num < 1 or num > 50 or num in user_numbers:
        num = int(input("Invalid or duplicate entry. Try again: "))
    user_numbers.append(num)

print("Your Lottery Numbers are:", user_numbers)
```

## 3. Comparing Results
Compare user-selected numbers with the randomly generated lottery numbers.

```python
# Find matching numbers
matches = set(lottery_numbers).intersection(user_numbers)

print(f"You matched {len(matches)} number(s): {sorted(matches)}")
```

## 4. Bonus: Enhanced Lottery Simulation
Add features to make the lottery simulation more exciting.

### a. Multiple Players
Allow multiple users to participate and find out who matches the most numbers.

```python
# Simulate multiple players
num_players = int(input("Enter the number of players: "))
players = {}

for player in range(1, num_players + 1):
    print(f"\nPlayer {player}, choose your numbers:")
    player_numbers = []
    for i in range(5):
        num = int(input(f"Enter number {i + 1}: "))
        while num < 1 or num > 50 or num in player_numbers:
            num = int(input("Invalid or duplicate entry. Try again: "))
        player_numbers.append(num)
    players[f"Player {player}"] = player_numbers

# Compare results for all players
for player, numbers in players.items():
    matches = set(lottery_numbers).intersection(numbers)
    print(f"{player} matched {len(matches)} number(s): {sorted(matches)}")
```

### b. Prize Tiers
Assign prize tiers based on the number of matches.

```python
# Prize tiers
prizes = {
    5: "Jackpot!",
    4: "Second Prize",
    3: "Third Prize",
    2: "Consolation Prize",
    1: "Better Luck Next Time",
    0: "No Matches, Try Again!"
}

# Display prize based on matches
matches = set(lottery_numbers).intersection(user_numbers)
print(f"You matched {len(matches)} number(s): {sorted(matches)}")
print("Prize:", prizes[len(matches)])
```

---

### Summary
This task introduces the `random` module and demonstrates its application in a fun lottery simulation. You can expand it further by adding more features or customizing the rules. Enjoy coding!
