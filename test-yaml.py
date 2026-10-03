import yaml
import json

meta = yaml.safe_load(open('apps/opencode/metadata.yaml'))
channel = meta['channels'][0]
if channel["tests"].get("type", "web") == "cli":
    print(json.dumps({"docker_run_args": "--entrypoint tail", "goss_args": "-f /dev/null"}))
else:
    print(json.dumps({"docker_run_args": "", "goss_args": ""}))
