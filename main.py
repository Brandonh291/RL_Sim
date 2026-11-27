# This is a project to create a priority of combat for a bot using Q-Learning in Reinforcement Learning system.
import time
from asyncio import wait
from random import randint

import numpy as np
import matplotlib.pyplot as plt

from Character import Character


# Actions (Columns)
# Define actions by an enumeration of integers where each integer represents an action to take
# To start, I am going to do just 2 Actions: Fast Attack and Slow Attack
# Fast Attack takes 1 second, and deals 1 damage
# Slow Attack takes 2 seconds, and deals 4 damage
# I am expecting that the system will take this and go with always the slow attack for higher dps without extra conditions

class SimulationData:
    def __init__(self, episodes, learn_rate, discount_factor,explore_prob,n_act, action_list= False, hp = 10000):
        self.hp = hp
        self.episodes = episodes
        self.learn_rate = learn_rate
        self.discount_factor = discount_factor
        self.explore_prob = explore_prob

        self.character = Character("MAGE",hp)
        self.Q_table = np.zeros(self.character.char_loadout.q_array_size)

    def get_state(self):
        return self.character.char_loadout.get_state()

    def choose_action(self):
        if np.random.rand() < self.explore_prob:
            action = np.random.randint(0, self.character.char_loadout.action_count)
        else:
            action = np.argmax(self.Q_table[self.character.char_loadout.curState])
        return action

    def take_action(self,act):
        self.character.char_loadout.select_action(act)

    def calculate_reward(self):
        return self.character.char_loadout.calculate_reward()

    def update_q_table(self, state, action, next_state, reward):
        self.Q_table[state, action] += self.learn_rate * (
                reward + self.discount_factor * np.max(self.Q_table[next_state]) - self.Q_table[state, action]
        )

    def display_results(self):
        print(self.Q_table)
        # q_values_grid = self.Q_table.reshape((self.n_state, self.n_act))
        #
        # plt.figure(figsize=(6, 6))
        # plt.imshow(q_values_grid, cmap='coolwarm', interpolation='nearest')
        # plt.colorbar(label='Q-value')
        # plt.title('Learned Q-values for Each State')
        #
        # # Build Y Tick Plot based on Steps
        # y_label = []
        #
        # for health in range(0,self.hp+1,1):
        #     if health > 0:
        #         y_label.append(f"{health} - {health-1}")
        #     else:
        #         y_label.append("0")
        # plt.yticks(np.arange(self.n_state),y_label)
        # plt.xticks(np.arange(self.n_act), ['Fast', 'Heavy'])
        # plt.gca().invert_yaxis()
        # plt.grid(True)
        #
        # # for i in range(self.n_state):
        # #     for j in range(self.n_act):
        # #         plt.text(j, i, f'{q_values_grid[i, j]:.2f}', ha='center', va='center', color='black')
        # plt.show()
        #print("Learned Q-table:")
        #print(sim.Q_table)
    def reset(self):
        self.character.char_loadout.reset()


    def run_simulation(self):
        for epoch in range(self.episodes):
            #health = np.random.randint(self.hp//2,self.hp)
            self.reset()
            current_state = self.get_state()

            while True:
                #print("Current State: ", current_state)

                # Determine Action
                action = self.choose_action()

                # Perform Action
                self.take_action(action)

                # Get Next State
                next_state = self.get_state()

                # Calculate Reward
                reward = self.calculate_reward()

                # Update Q_Table
                self.update_q_table(current_state, action, next_state, reward)
                #print("Q_Value: " + str(self.Q_table[current_state]))
                #time.sleep(.5)
                #print(Q_table)
                if self.character.char_loadout.tar_cur_hp <= 0:
                    break

                current_state = next_state




if __name__ == '__main__':
    #debugEnable = input("Enable debug mode? (y/n): ").strip().lower() in ["y", "yes","true", "t", "1"]
    #health_step, num_health_states = initialize_health_state()

    # Build Action List


    # Parameters
    epochs = 10000
    lRate = 0.8
    discFact = 0.95
    expProb = 0.1
    n_actions = 2

    sim = SimulationData(epochs,lRate, discFact, expProb,n_actions)
    sim.run_simulation()

    sim.display_results()


