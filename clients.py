import yaml
import os

def read_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'fullstack-repo', 'config.yaml')
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

config = read_config()
print(config['ServerIPAddress'])