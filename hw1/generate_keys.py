import rsa
import argparse

DEFAULT_KEY_SIZE = 2 ** 11


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('publicKey')
    argparser.add_argument('privateKey')
    argparser.add_argument('-s', default=DEFAULT_KEY_SIZE)
    args = argparser.parse_args()

    public, private = rsa.newkeys(args.s)

    with open(args.publicKey, 'wb') as f:
        f.write(public.save_pkcs1())

    with open(args.privateKey, 'wb') as f:
        f.write(private.save_pkcs1())


if __name__ == "__main__":
    main()
