# You need to install some python libraries which:

sklearn
pybullet
tensorboard
numpy
gym

# To run the trained model:

python3 run_robot.py

# To run the model with PPO:

In the run_robot.py file, comment on line 13 and remove comment on line 14

# To train the robot:

python3 train_robot.py

# If you want to train the robot with obstacles:

In the robot_gym_env.py file, remove comment on line 139

# In models folder, you can see the 3d model of the robot and obstacles.

# In trained folder, you can see the trained file.

# robot_gym_env.py is the environment of the trainings.

# run_robot.py is the file to load the trained model.

# train_robot.py is the train file for the robot training
