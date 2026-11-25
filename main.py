# This is a project to create a priority of combat for a bot using Q-Learning in Reinforcement Learning system.
import numpy as np
import matplotlib.pyplot as plt

# Steps for Q-Learning Algorithm

# Step 0. Create Base Q-Table
# Rows are states, columns are actions

# States (Rows)
# Enemy Health by % split by a range from 100 to 0%. 0% Being the Terminal State
# Going to split based on a set range per step
# so a step of 5 is 100% >= HEALTH > 95%
# Then 95% >= HEALTH > 90% etc down to 5% >= HEALTH > 0%, then a final state for 0%

# Calculate Current State based only on Health
def get_state(hp,h_step, n_states):
    if 100 >= hp >= 0:
        for state in range(int(n_states)):
            if (100 - h_step * state) >= hp > (100 - h_step * (state + 1)):
                return state
    else:
        if hp <= 0:
            return n_states-1
        print("Health State is out of range")
        return -1

    print("Did not find state")
    return -2

def initialize_health_state():
    check_input = False
    h_step = 0
    n_states = 0
    while check_input == False and h_step == 0:
        h_step = int(input("Health Step: "))
        n_states = 100 / h_step + 1
        if n_states.is_integer():
            check_input = True
    return int(h_step), int(n_states)


# Actions (Columns)
# Define actions by an enumeration of integers where each integer represents an action to take
# To start, I am going to do just 2 Actions: Fast Attack and Slow Attack
# Fast Attack takes 1 second, and deals 1 damage
# Slow Attack takes 2 seconds, and deals 4 damage
# I am expecting that the system will take this and go with always the slow attack for higher dps without extra conditions

# This update state is going to probably be much more complex as I add in real timing. For now lets try just doing
# a base setup with attacking without any consideration to timing.
def take_action(hp, act):
    if act == 0:
        hp -= 1
    if act == 1:
        hp -=12
    return hp
        # fast attack, low damage


class SimulationData:
    def __init__(self, episodes, learn_rate, discount_factor,explore_prob, n_state, n_act, h_step):
        self.Q_table = np.zeros((n_state, n_act))
        self.episodes = episodes
        self.learn_rate = learn_rate
        self.discount_factor = discount_factor
        self.explore_prob = explore_prob
        self.n_state = n_state
        self.n_act = n_act
        self.h_step = h_step


    def get_state(self,hp):
        if 100 >= hp >= 0:
            for state in range(int(self.n_state)):
                if (100 - self.h_step * state) >= hp > (100 - self.h_step * (state + 1)):
                    return state
        else:
            if hp <= 0:
                return self.n_state - 1
            print("Health State is out of range")
            return -1

        print("Did not find state")
        return -2

    def choose_action(self, state):
        if np.random.rand() < self.explore_prob:
            action = np.random.randint(0, n_actions)
        else:
            action = np.argmax(self.Q_table[state])
        return action

    def take_action(self,hp, act):
        if act == 0:
            hp -= 1
        if act == 1:
            hp -= 4
        return hp

    def calculate_reward(self, next_state):
        if next_state == self.n_state - 1:
            reward = 100
        else:
            reward = -1
        return reward

    def update_q_table(self, state, action, next_state, reward):
        self.Q_table[state, action] += self.learn_rate * (
                reward + self.discount_factor * np.max(self.Q_table[next_state]) - self.Q_table[state, action]
        )

    def display_results(self):
        print(self.Q_table)
        q_values_grid = self.Q_table.reshape((self.n_state, self.n_act))

        plt.figure(figsize=(6, 6))
        plt.imshow(q_values_grid, cmap='coolwarm', interpolation='nearest')
        plt.colorbar(label='Q-value')
        plt.title('Learned Q-values for Each State')

        # Build Y Tick Plot based on Steps
        y_Label = []
        health = 100
        for state in range(self.n_state):
            if health > 0:
                y_Label.append(f"{health}% - {health-self.h_step}%")
                health = health - self.h_step
            else:
                y_Label.append("0%")
        plt.yticks(np.arange(self.n_state),
                   y_Label)
        plt.xticks(np.arange(self.n_act), ['Fast', 'Heavy'])
        plt.gca().invert_yaxis()
        plt.grid(True)

        for i in range(num_health_states):
            for j in range(n_actions):
                plt.text(j, i, f'{q_values_grid[i, j]:.2f}', ha='center', va='center', color='black')

        plt.show()

        print("Learned Q-table:")
        print(sim.Q_table)

    def run_simulation(self):
        for epoch in range(self.episodes):
            health = 100
            current_state = self.get_state(health)

            while True:

                # Determine Action
                action = self.choose_action(current_state)

                # Perform Action
                health = take_action(health, action)

                # Get Next State
                next_state = self.get_state(health)

                # Calculate Reward
                reward = self.calculate_reward(next_state)

                # Update Q_Table
                self.update_q_table(current_state, action, next_state, reward)

                # print(Q_table)
                if next_state == num_health_states - 1:
                    break

                current_state = next_state




if __name__ == '__main__':
    #debugEnable = input("Enable debug mode? (y/n): ").strip().lower() in ["y", "yes","true", "t", "1"]
    health_step, num_health_states = initialize_health_state()

    # Parameters
    epochs = 10000
    lRate = 0.8
    discFact = 0.95
    expProb = 0.1
    n_actions = 2

    sim = SimulationData(epochs,lRate, discFact, expProb,num_health_states,n_actions,health_step)
    sim.run_simulation()

    sim.display_results()


