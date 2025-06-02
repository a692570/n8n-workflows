import os
import json
import re

WORKFLOWS_DIR = 'workflows'

# Sanitize to safe filename
def sanitize(name: str) -> str:
    name = re.sub(r'[\\/:*?"<>|]', '', name)
    name = name.strip()
    name = name.replace(' ', '_')
    return name[:100]  # limit length

for filename in os.listdir(WORKFLOWS_DIR):
    if not filename.endswith('.json'):
        continue
    path = os.path.join(WORKFLOWS_DIR, filename)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f'Skipping {filename}: {e}')
        continue
    name = data.get('name')
    if not name:
        if isinstance(data.get('nodes'), list) and data['nodes']:
            name = data['nodes'][0].get('name', 'Unnamed')
        else:
            name = 'Unnamed'
    new_basename = sanitize(name)
    new_file = new_basename + '.json'
    new_path = os.path.join(WORKFLOWS_DIR, new_file)
    if new_file == filename:
        continue
    base = new_basename
    count = 1
    while os.path.exists(new_path):
        count += 1
        new_file = f"{base}_{count}.json"
        new_path = os.path.join(WORKFLOWS_DIR, new_file)
    os.rename(path, new_path)
    print(f"Renamed {filename} -> {new_file}")
