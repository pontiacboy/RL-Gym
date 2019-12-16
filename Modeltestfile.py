def main():
    env = gym.make("MountainCar-v0")
    gamma = 0.9
    epsilon = .95

    trials = 1000
    trial_len = 500

    # updateTargetNetwork = 1000
    dqn_agent = success.model
    steps = []
    for trial in range(trials):
        cur_state = env.reset().reshape(1, 2)
        for step in range(trial_len):
            env.render()
            action = dqn_agent.act(cur_state)
            new_state, reward, done, _ = env.step(action)

            # reward = reward if not done else -20
            new_state = new_state.reshape(1, 2)
            dqn_agent.remember(cur_state, action, reward, new_state, done)

            dqn_agent.replay()  # internally iterates default (prediction) model
            dqn_agent.target_train()  # iterates target model

            cur_state = new_state
            if done:
                break
        if step >= 199:
            print("Failed to complete in trial {}".format(trial))
            print(step)
            if step % 10 == 0:
                dqn_agent.save_model("trial-{}.model".format(trial))
        else:
            print("Completed in {} trials".format(trial))
            print(step)
            dqn_agent.save_model("success.model")
            break
