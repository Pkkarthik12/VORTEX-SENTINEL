from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyEngine:

    def __init__(self):
        self.model = IsolationForest(contamination=0.05)

    def train(self, data):
        self.model.fit(data)

    def predict(self, values):
        return self.model.predict(values)

if __name__ == "__main__":
    sample = np.random.rand(100, 4)
    engine = AnomalyEngine()
    engine.train(sample)
    print("Anomaly Engine Ready")