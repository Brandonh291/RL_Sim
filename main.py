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

# Calculate Current State based only on Health
def get_state(health,h_step, n_states):
    if 100 >= health >= 0:
        for state in range(int(n_states)):
            if (100 - h_step * state) >= health > (100 - h_step * (state + 1)):
                return state
    else:
        print("Health State is out of range")
        return -1

    print("Did not find state")
    return -2

def initialize_health_state():
    check_input = False
    health_step = 0
    num_health_states = 0
    while check_input == False and health_step == 0:
        health_step = int(input("Health Step: "))
        num_health_states = 100 / health_step + 1
        if num_health_states.is_integer():
            check_input = True
    return health_step, num_health_states


# Actions (Columns)
# Define actions by an enumeration of integers where each integer represents an action to take
# To start, I am going to do just 2 Actions: Fast Attack and Slow Attack
# Fast Attack takes 1 second, and deals 1 damage
# Slow Attack takes 2 seconds, and deals 4 damage
# I am expecting that the system will take this and go with always the slow attack for higher dps without extra conditions

#def updateState(state, health, action):

# Step 1. Start at State

# Step 2. Choose Action

# Step 3. Perform Action

# Step 4. Measure Reward

# Step 5. Update Q-Table








# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    debugEnable = input("Enable debug mode? (y/n): ").strip().lower() in ["y", "yes","true", "t", "1"]

    health_step, num_health_states = initialize_health_state()

    if debugEnable:
        print("Number of Health States: " + str(num_health_states))
        print("States: ")
        healthVal = 100
        for i in range(int(num_health_states)):
            if healthVal != 0:
                print(f"State {i}: {healthVal}% >= X > {healthVal - health_step}%")
                healthVal -= health_step
            else:
                print(f"State {i}: 0% = X")

    # Test states
    if debugEnable:
        for i in range(0, 102, 4):
            print(f"State for health of {i}%: " + str(get_state(i, health_step, num_health_states)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
