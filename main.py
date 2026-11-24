# This is a project to create a priority of combat for a bot using Q-Learning in Reinforcement Learning system.
import numpy as np

# Steps for Q-Learning Algorithm

# Step 0. Create Base Q-Table
# Rows are states, columns are actions

# States (Rows)
# Enemy Health by % split by a range from 100 to 0%. 0% Being the Terminal State
# Going to split based on a set range per step
# so a step of 5 is 100% >= HEALTH > 95%
# Then 95% >= HEALTH > 90% etc down to 5% >= HEALTH > 0%, then a final state for 0%
healthStep = int(input("Health Step: "))

num_health_States = 100 / healthStep + 1

print("Number of Health States: " + str(num_health_States))
print("States: ")


# Step 1. Start at State

# Step 2. Choose Action

# Step 3. Perform Action

# Step 4. Measure Reward

# Step 5. Update Q-Table








# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
