import gymnasium as gym
from stable_baselines3 import SAC

model = SAC("MlpPolicy", verbose=1)

model.learn(total_timesteps=10000, log_interval=4)
