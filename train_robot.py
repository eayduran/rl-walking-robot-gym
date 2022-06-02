import time
import pybullet as p

from stable_baselines3 import PPO, A2C, SAC, TD3
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.env_util import make_vec_env
from robot_gym_env import RobotGymEnv

# Create environment from class
env = RobotGymEnv()
check_env(env)
models_dir = "trained/SAC"
# Training
# env = make_vec_env(lambda: env, n_envs=25)  # only for PPO
model = SAC('MlpPolicy', env, learning_starts=0, use_sde=False,
            use_sde_at_warmup=False, verbose=1, tensorboard_log="./robot-test/")
# model = PPO('MlpPolicy', env, batch_size=256, verbose=1,tensorboard_log="./ppo_robot/")

TIMES = 10000
for i in range(1, 200):
    model.learn(total_timesteps=TIMES,
                reset_num_timesteps=False, tb_log_name="SAC")
    model.save(f"{models_dir}/{TIMES*i}")
