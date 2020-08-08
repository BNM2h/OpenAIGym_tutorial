from env import ToyEnv
import random
import time

env=ToyEnv()
num_episodes=10

def main():
    for i in range(num_episodes):
        done=False
        state=env.reset()
        env.render()
        score=0
        while not done:
            action=random.randint(0,3)
            next_state,reward,done,info=env.step(action)
            env.render()
            state=next_state
            score+=reward
        print('done, score: ',score,'info:',info)
              
if __name__ == '__main__':
    main()