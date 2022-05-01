import re

def read_template(path):
    try:
        with open(path, 'r') as f:
            template = f.read()
        return template
    except Exception:
        raise FileNotFoundError

def parse_template(template):
    parts = re.findall(r'\{(.*?)\}', template)
    stripped = re.sub(r'\{(.*?)\}', '{}' , template)
    print(parts)
    print(stripped)
    return stripped, tuple(parts)

def merge(str, args):
    merged = str.format(*args)
    print(merged)
    return merged


