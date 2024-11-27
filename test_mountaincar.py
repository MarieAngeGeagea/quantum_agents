
from src.quantum.training import QLearningMountainCar
from config import Envs

def test_mountaincar():
    hyperparams = {
        'episodes': 5,
        'batch_size': 1,
        'gamma': 0.99,
        'circuit_depth': 1,
        'update_after': 1,
        'update_target_after': 1,
        'epsilon': 1.0,
        'epsilon_min': 0.1,
        'epsilon_decay': 0.9,
        'learning_rate': 0.01,
        'learning_rate_in': 0.01,
        'learning_rate_out': 0.01,
    }
    qlearning = QLearningMountainCar(
        hyperparams=hyperparams,
        env_name=Envs.MOUNTAINCAR,
        save=False,
        test=True
    )
    qlearning.perform_episodes()

if __name__ == "__main__":
    test_mountaincar()
