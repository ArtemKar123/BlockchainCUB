import rsa
import argparse


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('original')
    argparser.add_argument('signed')
    argparser.add_argument('key')
    args = argparser.parse_args()

    with open(args.original, 'rb') as f:
        original = f.read()

    with open(args.signed, 'rb') as f:
        signed = f.read()

    with open(args.key, 'rb') as f:
        key = rsa.PublicKey.load_pkcs1(f.read())

    try:
        rsa.verify(original, signed, key)
        print('File verified!')
    except rsa.VerificationError:
        print('Verification failed! :(')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
