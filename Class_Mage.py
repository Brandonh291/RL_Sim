# Mage Class
import random

import numpy as np

# Enumerate the current available actions
action_list = [
    "Frost Bolt",
    "Fireball",
    "Pyroblast",
    "Wand"
]

# This is the state list that the Mage class will care about and use to build the Q-table in main
# HP % , percentage of full of a creature, the actual HP value is going to be set in the sim
# Fire Ball DoT, this timing will be used to calculate the dot damage and remaining time is useful. I will do it in 0.1
#   Second increments.

state_list = [
    "HP %",
    "Mana %",
    "Fire Ball DoT Remaining Time",
    "Pyroblast Remaining Dot Time"
]

talent_list = [

]

mana_cost = [
    290,
    410,
    440,
    0
]

class Mage:
    def __init__(self,hp):
        # Sim Items
        self.time = 0
        self.damage = 0
        self.prev_time = 0

        # Character States
        # Health
        self.tar_total_hp = hp
        self.tar_cur_hp = hp
        self.hp_size = 101

        # Mana
        self.mana = 5103
        self.cur_mana = self.mana
        self.mana_size = 101

        # Spell States
        # Dot is based on the 8-second cooldown include 0.0 with 0.1 second increments
        self.fireball_dot_size = int(8 / 0.1 + 1)
        self.tar_fireball_time = 0

        # Dot based on 12 second cooldown 3 second proc
        self.pyroblast_dot_size = int(12 / 0.1 + 1)
        self.tar_pyroblast_time = 0

        # Build State and Action Variables
        self.action_count = len(action_list)
        self.action_labels = action_list
        self.state_labels = state_list

        self.curState = (self.tar_cur_hp, self.cur_mana, self.tar_fireball_time, self.tar_pyroblast_time)
        self.state_size = (self.hp_size, self.mana_size, self.fireball_dot_size, self.pyroblast_dot_size)
        self.q_array_size = (self.hp_size, self.mana_size, self.fireball_dot_size,self.pyroblast_dot_size, self.action_count)


    # The goal is that each action will have some values that need to be calculated and utilized at a given moment
    # The one issue is going to be DoTs because I need to figure out a way to integrate that into the overall system.
    # I think the best way to do that will be to perform a time_step inside here and return the time taken and calculate
    # All the damage done by the action chosen as well as previously chosen dots.
    # Problem is I want the system to also be fed the time left on DoTs then. That means that I should also return a
    # State space size and values for the sim to use
    # That would also make it useful so that each type of char is using the base initialization but custom fields
    def get_available_actions(self):
        available_actions = []

        for spell in range(len(mana_cost)):
            if mana_cost[spell] < self.mana:
                available_actions.append(spell)

        return available_actions

    def get_action(self, q_table, explore_prob):
        avail_act = ()

        for spell in range(len(mana_cost)):
            if mana_cost[spell] <= self.cur_mana:
                avail_act += (spell,)
                #avail_act.append(spell)

        if np.random.rand() < explore_prob:
            action = np.random.choice(avail_act)
        else:
            # Grab from the list of Q_tables in accordance with available actions
            avail = np.array(q_table[self.curState])
            avail = avail[list(avail_act)]
            action = np.argmax(avail)
            action = avail_act[action]

        return action

    def select_action(self, action):
        self.damage = self.tar_cur_hp
        self.prev_time = self.time
        if action == 0:
            self.take_action(0)
        if action == 1:
            self.take_action(1)
        if action == 2:
            self.take_action(2)
        if action == 3:
            self.take_action(3)

        self.damage -= self.tar_cur_hp
        self.prev_time = self.time - self.prev_time
        #print("Health Remaining: " + str(self.tar_cur_hp))



    def take_action(self, action):
        # Frost Bolt

        if action == 0:
            self.time_skip(3)
            self.cur_mana -= mana_cost[action]
            self.tar_cur_hp -= np.random.randint(470,505)
            #print("FROST BOLT: " + str(self.tar_cur_hp))

        # Fireball
        if action == 1:
            # Cast time
            self.time_skip(3.5)
            self.cur_mana -= mana_cost[action]
            self.tar_cur_hp -= np.random.randint(437,553)
            self.tar_fireball_time = 8
            #print("FIREBALL: " + str(self.tar_cur_hp))

        if action == 2:
            self.time_skip(6.0)
            self.cur_mana -= mana_cost[action]
            self.tar_cur_hp -= np.random.randint(547,674)
            self.tar_pyroblast_time = 12

        if action == 3:
            self.time_skip(1.8)
            self.tar_cur_hp -= np.random.randint(78,147)

    def get_state(self):
        # This is returning an array of the positions for each state dimension
        if self.tar_cur_hp <= 0:
            self.tar_cur_hp = 0
        if self.cur_mana <= 0:
            self.cur_mana = 0

        self.curState = (int(self.tar_cur_hp / self.tar_total_hp * 100),int(self.cur_mana / self.mana * 100), int(self.tar_fireball_time / 0.1), int(self.tar_pyroblast_time / 0.1))

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
            # Reward is a flat 100
            reward = 10
        else:
            # Reward is based on the time taken for the task
            reward = -0.1 + 0.05* (self.damage/self.tar_total_hp*100)

        return reward

    def reset(self):
        self.tar_cur_hp = self.tar_total_hp
        self.tar_fireball_time = 0
        self.time = 0
        self.cur_mana = self.mana