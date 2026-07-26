import json
import yaml

config = {
    "server": "prod",
    "port": 80,
    "status": "active"
}

with open("config.json", "w") as file:
    json.dump(config, file)

with open("config.json", "r") as file:
    config = json.load(file)

config["status"] = "maintenance"

with open("config.yaml", "w") as file:
    yaml.dump(config, file)
