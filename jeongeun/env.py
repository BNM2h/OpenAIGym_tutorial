import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import random
class ToyEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    self.action_space = spaces.Discrete(4)
    self.observation_space = spaces.Box(-1,3, dtype=np.int8,shape=(5,5))
    self.tmap=np.zeros((5,5))
    self.num_goal=3
    self.goal_left=self.num_goal
    self.current=[0,0]
    self.done=False

  def step(self, action):
    self.tmap[self.current[0],self.current[1]]=0
    current=self.current
    reward=0
    if action==0:
      if self.current[1]==4:
        #self.done=True
        print('collision')
        reward=-1
      else:
        current=[self.current[0],self.current[1]+1]
        reward=-0.1
    if action==1:
      if self.current[0]==4:
        #self.done=True
        print('collision')
        reward=-1
      else:
        current=[self.current[0]+1,self.current[1]]
        reward=-0.1
    if action==2:
      if self.current[1]==0:
        #self.done=True
        print('collision')
        reward=-1
      else:
        current=[self.current[0],self.current[1]-1]
        reward=-0.1
    if action==3:
      if self.current[0]==0:
        #self.done=True
        print('collision')
        reward=-1
      else:
        current=[self.current[0]-1,self.current[1]]
        reward=-0.1
    
    self.current=current
    
    if self.tmap[self.current[0],self.current[1]]==2:
      self.tmap[self.current[0],self.current[1]]=1
      self.goal_left-=1
      print('goal')
      reward=1
    else:
      self.tmap[self.current[0],self.current[1]]=1
    
    if self.goal_left==0:
      print('done')
      self.done=True
    
    info=self.goal_left
    
    return self.tmap,reward,self.done,info

  def reset(self):
    self.done=False
    self.goal_left=self.num_goal
    self.tmap=np.zeros((5,5))
    self.tmap[0,0]=1
    self.current=[0,0]
    
    for i in range(self.num_goal):
      check=True
      while check:
        goal_x=np.random.randint(0,5)
        goal_y=np.random.randint(0,5)
        if self.tmap[goal_x,goal_y]==2:
          pass
        else:  
          self.tmap[goal_x,goal_y]=2
          check=False
    
    return self.tmap
    # 1: where i am, 2: goal 0: default


  def render(self, mode='human', close=False):
    print(self.tmap)
    pass