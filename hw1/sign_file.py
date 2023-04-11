import rsa
import argparse

HASH_FUNCTION = 'SHA-256'

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('input')
    argparser.add_argument('output')
    argparser.add_argument('key')
    args = argparser.parse_args()

    with open(args.input, 'rb') as f:
        content = f.read()

    with open(args.key, 'rb') as f:
        key = rsa.PrivateKey.load_pkcs1(f.read())

    with open(args.output, 'wb') as f:
        f.write(rsa.sign(content, key, HASH_FUNCTION))


if __name__ == "__main__":
    main()
