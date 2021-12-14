#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 04:16:10 2021

@author: maryam
"""

import gym
env = gym.make('Walker2d-v2')

observation = env.reset()

print(len(observation))
print(env.action_space)

done = False
while not done:

    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    print(action)
        
    env.render()
 
