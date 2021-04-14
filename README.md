## Status

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-brightgreen.svg)](https://www.gnu.org/licenses/gpl-3.0)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/JavDomGom/Identity-Based-Encryption)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)

## Basic overview

PoC communication between two devices, for example two vehicles, using Identity-Based-Encryption in Python 3.

## Dependencies

```bash
~$ sudo apt install libmpc-dev
~$ pip3 install gmpy2 pycocks bitarray
~$ pip3 install pyjwt
```

## How it works

Import this packages:

```python
import jwt
import sys

from cocks.cocks import CocksPKG, Cocks

import vehicle
```

Each vehicle or device generates its own digital identity (with JWT) using its public data and private key.

```python
A_private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMII...GA=\n-----END RSA PRIVATE KEY-----'
A_public_key = b'-----BEGIN PUBLIC KEY-----\nMIG...QAB\n-----END PUBLIC KEY-----'
A = vehicle.Vehicle(
    'Ford', 'Focus', 2021, '9f7h4sqc', A_private_key, A_public_key
)
A_pub_identity = A.encodeIdentity()
print(f'A public identity: {A_pub_identity}')
```

```python
B_private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMII...AmI\n-----END RSA PRIVATE KEY-----'
B_public_key = b'-----BEGIN PUBLIC KEY-----\nMIG...QAB\n-----END PUBLIC KEY-----'
B = vehicle.Vehicle(
    'Tesla', 'Model S', 2020, 'a305d39e', B_private_key, B_public_key
)
B_pub_identity = B.encodeIdentity()
print(f'B public identity: {B_pub_identity}')
```

And create an `CocksPKG` object:
```python
PKG = CocksPKG(2048)
```

And now follow the next steps:

<p align="center"><img src="https://github.com/JavDomGom/Identity-Based-Encryption/blob/main/img/Identity-Based-Encryption-explanation.png"></p>

1. Vehicle A asks the PKG for the public data of vehicle B.

    ```python
    pkg_private_key, pkg_public_hashed_identity = PKG.extract(
        B_pub_identity.decode()
    )
    pkg_public_modulus = PKG.n
    ```

2. PKG, which has the public key of A (and of all vehicles), verifies the identity signature of vehicle A using `A_pub_identity`.

    ```python
    try:
        jwt.decode(A_pub_identity, A_public_key, algorithms=['RS256'])
    except Exception as e:
        print(f'ERROR: {e}')
        sys.exit(1)
    ```

3. If the previous verification was successful, PKG returns to vehicle A only vehicle B's `pkg_public_hashed_identity` and `pkg_public_modulus`.

    ```python
    print(f'pkg_public_hashed_identity: {pkg_public_hashed_identity}')
    print(f'pkg_public_modulus: {pkg_public_modulus}')
    ```

4. Vehicle A encrypts the message using vehicle B's `pkg_public_modulus`, `B_pub_identity`, and `pkg_public_hashed_identity`.

    ```python
    cocks = Cocks(pkg_public_modulus)
    encrypted_msg = cocks.encrypt(b'Hola mundo!', pkg_public_hashed_identity)
    ```

5. Vehicle A sends the encrypted message to vehicle B.

    ```python
    print(f'encrypted_msg: {encrypted_msg}')
    ```

6. Vehicle B asks the PKG for its `pkg_private_key` and `pkg_public_hashed_identity`.

    ```python
    print(f'pkg_private_key: {pkg_private_key}')
    ```

7. PKG, which has the public key of B (and of all vehicles), verifies the identity signature of vehicle B using `B_pub_identity`.

    ```python
    try:
        jwt.decode(B_pub_identity, B_public_key, algorithms=['RS256'])
    except Exception as e:
        print(f'ERROR: {e}')
        sys.exit(1)
    ```

8. Vehicle B decrypts the encrypted message sent to it by vehicle A using `pkg_private_key` and `pkg_public_hashed_identity`.

    ```python
    decrypted_msg = cocks.decrypt(
        encrypted_msg,
        pkg_private_key,
        pkg_public_hashed_identity
    ).decode()
    print(f'decrypted_msg: {decrypted_msg}')
    ```

## Generate RSA key pair (Pub/Priv)

RSA private key:

```bash
~$ openssl genrsa 1024
Generating RSA private key, 1024 bit long modulus (2 primes)
...........+++++
................................+++++
e is 65537 (0x010001)
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQDYT4uFPypk5PYcjnzPavD3//zDdDRkanfGcE95oCOx5zbfSB8D
c/YPL1NeunwbGxVsY5PDXx8qDvpmTARQsE/89EjDbe4uRMtW2C5YYDkvxO/ZkLCF
waIG3/0qSnwfz8fIuL8nvGAhUPBbgWbtK3qTsif5CCvahuWrUH2WHGMPvQIDAQAB
AoGASdZlVten/gbWKAtPeXIUzWMZghKRq9FYD2nZBzht1tWJOpCg3Yng7XAHMmfP
42TMXFJlZyR6O94fBXpfYre8pYiHSwBTC2LurBHGuyZ2X0sjuYV7q4HAgtj3fOVO
67wq0Zaf4eaZgdngePS1EHqNMpbxaUWb1Xuk2GIUBNYd4vUCQQDuBE/1pZZ4eufn
ZsJ0ZiMoAcadW1MM08SSGVvaEc0nB6U7UUyXZYVfIjwd6MNwkWTsWeauGnD13KFX
HKSWjHZ/AkEA6KdlXVKKYwACXE3RQMBRuacVSFfx0UPj4SDKLzxjfcwTrntF6svM
8NQqqIfRsGjX8EtUGvTfG4fmaLICZnazwwJACrthC5dyyG3qRPHKNMtiLGygEvpK
LVrjEx9Xl+aTlH3wwlLxHCZ0tAxsH4EeRtYXcdy/3PvOOhe/opjlBvDAawJAYjsj
klaidZBwbrawjm1lVETWuJfhUyEeG1Tz6SPPQjMjcD0+VRe9rUV3yXanM5vg6OV1
Wnhfp0knILdgShD+bwJBAKrumWs0PA5k8qN8S45SIT8W/foYm8dbESV+anEvn8RY
j/DhHttjJ+RSWpHv/gHSNKTYCt9jJp2tGFKGQGkqLGA=
-----END RSA PRIVATE KEY-----
```

```bash
~$ private_key="""-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQDYT4uFPypk5PYcjnzPavD3//zDdDRkanfGcE95oCOx5zbfSB8D
c/YPL1NeunwbGxVsY5PDXx8qDvpmTARQsE/89EjDbe4uRMtW2C5YYDkvxO/ZkLCF
waIG3/0qSnwfz8fIuL8nvGAhUPBbgWbtK3qTsif5CCvahuWrUH2WHGMPvQIDAQAB
AoGASdZlVten/gbWKAtPeXIUzWMZghKRq9FYD2nZBzht1tWJOpCg3Yng7XAHMmfP
42TMXFJlZyR6O94fBXpfYre8pYiHSwBTC2LurBHGuyZ2X0sjuYV7q4HAgtj3fOVO
67wq0Zaf4eaZgdngePS1EHqNMpbxaUWb1Xuk2GIUBNYd4vUCQQDuBE/1pZZ4eufn
ZsJ0ZiMoAcadW1MM08SSGVvaEc0nB6U7UUyXZYVfIjwd6MNwkWTsWeauGnD13KFX
HKSWjHZ/AkEA6KdlXVKKYwACXE3RQMBRuacVSFfx0UPj4SDKLzxjfcwTrntF6svM
8NQqqIfRsGjX8EtUGvTfG4fmaLICZnazwwJACrthC5dyyG3qRPHKNMtiLGygEvpK
LVrjEx9Xl+aTlH3wwlLxHCZ0tAxsH4EeRtYXcdy/3PvOOhe/opjlBvDAawJAYjsj
klaidZBwbrawjm1lVETWuJfhUyEeG1Tz6SPPQjMjcD0+VRe9rUV3yXanM5vg6OV1
Wnhfp0knILdgShD+bwJBAKrumWs0PA5k8qN8S45SIT8W/foYm8dbESV+anEvn8RY
j/DhHttjJ+RSWpHv/gHSNKTYCt9jJp2tGFKGQGkqLGA=
-----END RSA PRIVATE KEY-----
"""
```

Extract public key:

```bash
~$ echo "$private_key" | sed -e 's/^[ ]*//' | openssl rsa -pubout
writing RSA key
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDYT4uFPypk5PYcjnzPavD3//zD
dDRkanfGcE95oCOx5zbfSB8Dc/YPL1NeunwbGxVsY5PDXx8qDvpmTARQsE/89EjD
be4uRMtW2C5YYDkvxO/ZkLCFwaIG3/0qSnwfz8fIuL8nvGAhUPBbgWbtK3qTsif5
CCvahuWrUH2WHGMPvQIDAQAB
-----END PUBLIC KEY-----
```

## How to run

```bash
~$ python3 main.py
```

## References and documents

* https://en.wikipedia.org/wiki/Identity-based_encryption
* https://github.com/cgshep/pycocks
* https://en.wikipedia.org/wiki/JSON_Web_Token
* [Using Attribute-Based Encryption on IoT Devices
with instant Key Revocation](https://core.ac.uk/download/pdf/195320109.pdf)
