# RSA
## Generating keys
```shell
python3 generate_keys.py pub.pem private.pem
```
## Signing file
```shell
python3 sign_file.py hello_world.txt signed private.pem
```
## Verify
```shell
python3 verife_signed.py hello_world.txt signed pub.pem
```