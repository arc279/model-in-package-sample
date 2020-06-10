import importlib.resources
import pickle

def load_model(module, fillename="model.pkl"):
    b = importlib.resources.read_binary(module, fillename)
    return pickle.loads(b)


from . import version
__version__ = version.VERSION
