import yaml

data_to_yaml = {
    "key_1": [1, 'cde', 87],
    "key_2": 246,
    "key_3": {
        "2Ж": "1,50",
        "7Я": "fghj"
    }
}

with open('file.yaml', 'w') as f_n:
    yaml.dump(data_to_yaml, f_n, default_flow_style=False, allow_unicode=True)

with open('file.yaml') as f_n:
    print(f_n.read())
