from gymnasium import Env, spaces
import numpy as np
from dataset import active_power
import pandas as pd


class EntornoMicroRed(Env):
    def __init__(self, df: pd.DataFrame):
        super().__init__()

        self.dataset = pd.astype(np.float.32).values
        # cantidad  de acciones
        self.action_space = spaces.Discrete(3) # Usar bateria, usar Energia Solar y usar Hidrogeno verde

        # cantidad de caracteristicas de entrenamiento
        self.n_features = self.dataset.shape[1]
        # cantidad de pasos del entorno
        self.n_steps = len(self.dataset)


        # espacios minimos y maximos de la caja
        limites_inferiores = np.max(self.dataset, axis=0)
        limites_superiores = np.min(self.dataset, axis=0)

        # paso inicial del modelo, fila 0 del dataset
        self.paso_actual = 0


        def reset():
            datos_actuales = self.dataset[self.paso_actual]
            self.paso_actual = 0
            self.paso_actual += 1


        def recompensa() -> None:
            return None
