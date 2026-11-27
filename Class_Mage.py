# Mage Class
import random

import numpy as np

# Enumerate the current available actions
action_list = [
    "Frost Bolt",
    "Fireball",
    "Pyroblast"
]

# This is the state list that the Mage class will care about and use to build the Q-table in main
# HP % , percentage of full of a creature, the actual HP value is going to be set in the sim
# Fire Ball DoT, this timing will be used to calculate the dot damage and remaining time is useful. I will do it in 0.1
#   Second increments.

state_list = [
    "HP %",
    "Fire Ball DoT Remaining Time",
    "Pyroblast Remaining Dot Time"
]

class Mage:
    def __init__(self,hp):
        self.action_count = len(action_list)
        self.action_labels = action_list
        self.state_labels = state_list
        self.time = 0


        # Get array sizes
        # HP is based on 100% to 0% in 1 % increments
        self.hp_size = 101
        self.tar_total_hp = hp
        self.tar_cur_hp = hp

        # Dot is based on the 8-second cooldown include 0.0 with 0.1 second increments
        self.fireball_dot_size = int(8/0.1 + 1)
        self.tar_fireball_time = 0

        # Dot based on 12 second cooldown 3 second proc
        self.pyroblast_dot_size = int(12/0.1 + 1)
        self.tar_pyroblast_time = 0


        self.curState = (self.tar_cur_hp, self.tar_fireball_time, self.tar_pyroblast_time)
        self.q_array_size = (self.hp_size, self.fireball_dot_size,self.pyroblast_dot_size, self.action_count)


    # The goal is that each action will have some values that need to be calculated and utilized at a given moment
    # The one issue is going to be DoTs because I need to figure out a way to integrate that into the overall system.
    # I think the best way to do that will be to perform a time_step inside here and return the time taken and calculate
    # All the damage done by the action chosen as well as previously chosen dots.
    # Problem is I want the system to also be fed the time left on DoTs then. That means that I should also return a
    # State space size and values for the sim to use
    # That would also make it useful so that each type of char is using the base initialization but custom fields
    def select_action(self, action):
        if action == 0:
            self.take_action(0)
        if action == 1:
            self.take_action(1)
        if action == 2:
            self.take_action(2)

        #print("Health Remaining: " + str(self.tar_cur_hp))


    def take_action(self, action):
        # Frost Bolt
        if action == 0:
            self.time_skip(3)
            self.tar_cur_hp -= np.random.randint(470,505)
            #print("FROST BOLT: " + str(self.tar_cur_hp))

        # Fireball
        if action == 1:
            # Cast time
            self.time_skip(3.5)
            self.tar_cur_hp -= np.random.randint(437,553)
            self.tar_fireball_time = 8
            #print("FIREBALL: " + str(self.tar_cur_hp))

        if action == 2:
            self.time_skip(6.0)
            self.tar_cur_hp -= np.random.randint(547,674)
            self.tar_pyroblast_time = 12

    def get_state(self):
        # This is returning an array of the positions for each state dimension
        if self.tar_cur_hp <= 0:
            self.tar_cur_hp = 0

        self.curState = (int(self.tar_cur_hp / self.tar_total_hp * 100), int(self.tar_fireball_time / 0.1), int(self.tar_pyroblast_time / 0.1))

        return self.curState

    def time_skip(self, time):
        # Do time stuff
        time_to_pass = time

        while time_to_pass > 0:
            # Check DoTs
            if self.tar_fireball_time > 0:
                self.tar_fireball_time -= 0.1
                if self.tar_fireball_time in [6,4,2,0]:
                    self.tar_cur_hp -= 15 # This needs to be changeable later

            if self.tar_pyroblast_time > 0:
                self.tar_pyroblast_time -= 0.1
                if self.tar_pyroblast_time in [9,6,3,0]:
                    self.tar_cur_hp -= 53
            time_to_pass -= 0.1

        self.time += time

    def calculate_reward(self):
        if self.tar_cur_hp <= 0:
            # DPS
            reward = self.tar_cur_hp/self.time
        else:
            # Else we want the model to focus first on lower HP, an second on overall time (actions) taken
            #reward = self.time* -0.1 + ((self.tar_cur_hp / self.tar_total_hp)*100) * -0.2
            reward = -0.1

        return reward

    def reset(self):
        self.tar_cur_hp = self.tar_total_hp
        self.tar_fireball_time = 0
        self.time = 0