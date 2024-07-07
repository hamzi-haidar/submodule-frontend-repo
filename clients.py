import os
import yaml

class Client:
    def __init__(self):
        yaml_path = os.path.join(os.path.dirname(__file__), '../config.yaml')
        with open(yaml_path, 'r') as file:
            self.yaml = yaml.safe_load(file)
      
client = Client()

print(client.yaml["serverIPAddress"])



