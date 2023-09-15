import requests
import json
from base_structs import Project, Version  # assuming base_structs is a Python module containing the definitions

def get_project_version(project_name: str, project_version: int, api_key: str):
    url = f"https://getpipeline-kk2bzka6nq-uc.a.run.app/?projectName={project_name}&version={project_version}&apiKey={api_key}"
    response = requests.get(url)
    response.raise_for_status()  # this will raise an HTTPError if the HTTP request returned an unsuccessful status code

    res_json = response.json()
    project = json.loads(json.dumps(res_json["project"]), object_hook=Project)
    version = json.loads(json.dumps(res_json["version"]), object_hook=Project)
    # Assuming that Project and Version classes or dataclasses have a way to parse from dict or you just want to keep them as dict
    return (
        project,
        version,
    )

# Note: If Project and Version have some parsing methods, you might need to invoke them to convert res_json["project"] and res_json["version"] to respective types.