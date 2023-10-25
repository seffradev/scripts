import sys

keys = {
    ',': 'w',
    '.': 'e',
    ';': 'z',
    '\'': 'q',
    'a': 'a',
    'b': 'n',
    'c': 'i',
    'd': 'h',
    'e': 'd',
    'f': 'y',
    'g': 'u',
    'h': 'j',
    'i': 'g',
    'j': 'c',
    'k': 'v',
    'l': 'p',
    'm': 'm',
    'n': 'l',
    'o': 's',
    'p': 'r',
    'q': 'x',
    'r': 'o',
    't': 'k',
    'u': 'f',
    'v': '.',
    'w': ',',
    'x': 'b',
    'y': 't',
    'z': '-',
}

def dedvorak(message):
    """Converts a message written with QWERTY-muscles on a Dvorak layout to
    comprehensible English."""
    converted = []
    for c in message:
        try:
            converted.append(keys[c])
        except:
            converted.append(c)

    return ''.join(converted)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python dedvorak.py <message>')
        sys.exit(1)

    sys.argv.pop(0)
    for idx, i in enumerate(sys.argv):
        if idx == len(sys.argv) - 1:
            print(dedvorak(i))
        else:
            print(dedvorak(i), end=' ')
