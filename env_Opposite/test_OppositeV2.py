
from env_Opposite import EnvOpposite
import random

if __name__ == '__main__':
    env = EnvOppositeV2(7)
    max_iter = 100000
    for i in range(max_iter):
        env.render()
        action_list = [random.randint(0, 4), random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)]
        reward, done = env.step(action_list)
        print("iter= ", i, 'reward', reward)
        if done:
            print('find goal, reward')
            env.reset()
