# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:00:11 2023

@author: SanthosRaj
"""

import os

from stable_baselines3.common.env_util import make_vec_env

cwd = os.getcwd().replace('/reinforcement_learning', '')
os.chdir(cwd)

from dataset import Dataset
import gym 
import gym_anytrading
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, VecNormalize
import pandas as pd
import quantstats as qs

data_binance = Dataset().get_data(days=30, ticker='BTCUSDT', ts='5m')

df = data_binance.copy()[['open', 'high', 'low', 'close', 'volume']]
df = df.reset_index()
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
df = df.set_index('Date')

log_dir = r"D:\Santhosraj Machine learning\spyder\college_project\trading\RL\tmp"
stats_path = os.path.join(log_dir, "vec_normalize.pkl")

window_size = 50
start_index = window_size
end_index = len(df)
num_cpu = os.cpu_count()


def create_env(df, start_index, end_index, window_size):
    env = gym.make('forex-v0', df=df,  frame_bound=(start_index,
                   end_index), window_size=window_size)
    env.trade_fee = 0
    return env


def env_maker():
    return create_env(df, start_index, end_index, window_size)


env = make_vec_env(
    lambda: env_maker(),
    n_envs=num_cpu,
    seed=0,
    vec_env_cls=DummyVecEnv
)

# Automatically normalize the input features and reward
env = VecNormalize(env, norm_obs=True, norm_reward=True, clip_obs=10.)

model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="./tensorboard_logs/")
model.learn(total_timesteps=2500000)

model.save(f"{log_dir}/ppo_halfcheetah")
env.save(stats_path)

#testing the model

env = make_vec_env(lambda : env_maker(),n_envs = num_cpu, seed = 0 , vec_env_cls = DummyVecEnv)
env = VecNormalize.load(stats_path, env)
env.training = False
env.norm_reward = False

#load Agent
model = PPO.load(f"{log_dir}/ppo_halfcheetah", env = env )

obs = env.reset()

results = []

while True :
    action , state = model.predict(obs)
    obs,reward , done , info = env.step(action)
    profit = {f'env_{num}':float(i["total_profit"]) for num , i in enumerate(info)}
    results.append(profit)
    if done.all():
        break
results = pd.DataFrame(results)

results.tail(1000).plot(figsize = (40,10))

qs.extend_pandas()

networth = pd.Series(results["env_0"].values, index = df.index[start_index+1:end_index])
returns = networth.iloc[1:]

qs.reports.full(returns)