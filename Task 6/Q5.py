class Model:
    def predict(self, data): pass

class LinearModel(Model):
    def predict(self, data): return "Linear Prediction"

class TreeModel(Model):
    def predict(self, data): return "Tree Prediction"

def run_prediction(model, data):
    return model.predict(data)
