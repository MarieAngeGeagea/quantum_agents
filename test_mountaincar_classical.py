
from src.quantum.training import QLearningMountainCarClassical
from config import Envs

def test_mountaincar_classical():
    hyperparams = {
        'episodes': 5,
        'batch_size': 1,
        'gamma': 0.99,
        'update_after': 1,
        'update_target_after': 1,
        'epsilon': 1.0,
        'epsilon_min': 0.1,
        'epsilon_decay': 0.9,
        'learning_rate': 0.01,
        'n_hidden_layers': 2,
        'hidden_layer_config': [64, 64],
    }
    qlearning = QLearningMountainCarClassical(
        hyperparams=hyperparams,
        env_name=Envs.MOUNTAINCAR,
        save=False,
        test=True
    )
    qlearning.perform_episodes()

if __name__ == "__main__":
    test_mountaincar_classical()
