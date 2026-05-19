from src.report import io_ops

def load_config(path):

    config = io_ops.read_yaml(path)
    
    return config

def parse_params(config):
    if 'params' not in config:
        raise ValueError("params not in config")
    return config["params"]
    