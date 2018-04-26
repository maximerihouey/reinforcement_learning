import numpy as np
import gym

env = gym.make('GuessingGame-v0')
env.reset()

# applying dichotomy
def dichotomize(upper, lower):
    return (upper + lower) / 2.0

upper_bound = 1000.0
lower_bound = -1000.0

done = False
target = env.env.number
while not done:
    guess = dichotomize(upper_bound, lower_bound)
    print("[{}, {}, {}]".format(lower_bound, guess, upper_bound))

    observation, reward, done, info = env.step(np.array([guess]))

    if observation == 1:
        # Guess is lower than the target
        lower_bound = guess
    elif observation == 2:
        # Guess is equal to the target
        print("YASSSS")
    elif observation == 3:
        # Guess is higher than the target
        upper_bound = guess
    else:
        raise("Problem")


print("Guess: {} | Target: {}".format(guess, target))

