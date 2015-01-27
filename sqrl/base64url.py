import base64


def encode(value):
    return base64.urlsafe_b64encode(str(value)).rstrip('=')

def decode(value):
    return base64.urlsafe_b64decode(str(value) + '=' * (4 - len(value) % 4))

def decode_dict(value):
    text = decode(str(value))
    output = {}
    for pair in text.split('\r\n'):
        if '=' in pair:
            key, val = pair.split('=')
            output[key] = val
    return output
