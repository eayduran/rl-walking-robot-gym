import time
import pybullet as p

from stable_baselines3 import PPO, A2C, SAC
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.env_util import make_vec_env
from robot_gym_env import RobotGymEnv

# Create environment from class
env = RobotGymEnv()
check_env(env)

model = SAC.load("trained/sac_trained")
# model = PPO.load("trained/ppo_trained")

obs = env.reset()

for _ in range(500):
    action, _state = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    print(reward)
    env.render(mode="human")
    if done:
        obs = env.reset()
    time.sleep(1./140.)
