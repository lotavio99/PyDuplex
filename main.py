from hashlib import md5
import os


def generate_hash(file):
    file = open(file, 'rb').read()
    return md5(file).hexdigest()


def map_files(path):
    for r, p, f in os.walk(path):
        for file in f:
            complete_path = os.path.join(r, file)
            HASH = generate_hash(complete_path)
            print(complete_path, HASH)


def main():
    initial_path = r""
    map_files(initial_path)


if __name__ == '__main__':
    main()