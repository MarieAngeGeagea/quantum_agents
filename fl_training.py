from config import Envs, BASE_PATH
from src.quantum.training import QLearningMountainCar

hyperparams = {
    # Adjust hyperparameters for MountainCar
    'episodes': 5000,
    'max_steps': 200,
    'gamma': 0.99,
    'epsilon': 1,
    'epsilon_decay': 0.999,
    'epsilon_min': 0.1,
    'learning_rate': 0.01,
}

qlearning = QLearningMountainCar(
    hyperparams,
    Envs.MOUNTAINCAR,
    save=True,
    save_as='mc_results',
    path=BASE_PATH + 'mountain_car/mc_q_learning/',
)

qlearning.perform_episodes()
