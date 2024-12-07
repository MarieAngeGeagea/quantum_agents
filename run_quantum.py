import tensorflow as tf
from src.utils.limit_thread_usage import set_thread_usage_limit
set_thread_usage_limit(10, tf)

from config import BASE_PATH, Envs
from parallelize import parallelize_mc_q


hyperparams = {
    'episodes': [15000],
    'batch_size': [32],
    'epsilon': [1],
    'epsilon_decay': [0.75],
    'epsilon_min': [0.01],
    'gamma': [0.85],
    'update_after': [10],
    'update_target_after': [30],
    'learning_rate': [0.001],
    'learning_rate_in': [0.001],
    'learning_rate_out': [0.1],
    'circuit_depth': [15],
    'epsilon_schedule': ['linear'],
    'use_reuploading': True,
    'trainable_scaling': True,
    'trainable_output': True,
    'output_factor': 1,
    'reps': 1,
    'env': Envs.MOUNTAINCAR,
    'save': True,
    'test': False
}


if __name__ == '__main__':
    parallelize_mc_q(hyperparams, BASE_PATH + 'mountaincar/mountaincarQ/')
