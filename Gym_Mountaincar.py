import gym
env = gym.make('MountainCarContinuous-v0') # try for different environements
observation = env.reset()
iteration = 0
for t in range(4000):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        iteration = iteration +1
        if(reward > 99):
            print(reward + ' Iteration' +iteration)
            env.close()
env.close()