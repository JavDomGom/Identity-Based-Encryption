import jwt
import sys

from cocks.cocks import CocksPKG, Cocks

import vehicle

""" Vehicle A generates its own digital identity using its public data and
private key. """
A_private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQDYT4uFPypk5PYcjnzPavD3//zDdDRkanfGcE95oCOx5zbfSB8D\nc/YPL1NeunwbGxVsY5PDXx8qDvpmTARQsE/89EjDbe4uRMtW2C5YYDkvxO/ZkLCF\nwaIG3/0qSnwfz8fIuL8nvGAhUPBbgWbtK3qTsif5CCvahuWrUH2WHGMPvQIDAQAB\nAoGASdZlVten/gbWKAtPeXIUzWMZghKRq9FYD2nZBzht1tWJOpCg3Yng7XAHMmfP\n42TMXFJlZyR6O94fBXpfYre8pYiHSwBTC2LurBHGuyZ2X0sjuYV7q4HAgtj3fOVO\n67wq0Zaf4eaZgdngePS1EHqNMpbxaUWb1Xuk2GIUBNYd4vUCQQDuBE/1pZZ4eufn\nZsJ0ZiMoAcadW1MM08SSGVvaEc0nB6U7UUyXZYVfIjwd6MNwkWTsWeauGnD13KFX\nHKSWjHZ/AkEA6KdlXVKKYwACXE3RQMBRuacVSFfx0UPj4SDKLzxjfcwTrntF6svM\n8NQqqIfRsGjX8EtUGvTfG4fmaLICZnazwwJACrthC5dyyG3qRPHKNMtiLGygEvpK\nLVrjEx9Xl+aTlH3wwlLxHCZ0tAxsH4EeRtYXcdy/3PvOOhe/opjlBvDAawJAYjsj\nklaidZBwbrawjm1lVETWuJfhUyEeG1Tz6SPPQjMjcD0+VRe9rUV3yXanM5vg6OV1\nWnhfp0knILdgShD+bwJBAKrumWs0PA5k8qN8S45SIT8W/foYm8dbESV+anEvn8RY\nj/DhHttjJ+RSWpHv/gHSNKTYCt9jJp2tGFKGQGkqLGA=\n-----END RSA PRIVATE KEY-----'  # noqa: E501
A_public_key = b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDYT4uFPypk5PYcjnzPavD3//zD\ndDRkanfGcE95oCOx5zbfSB8Dc/YPL1NeunwbGxVsY5PDXx8qDvpmTARQsE/89EjD\nbe4uRMtW2C5YYDkvxO/ZkLCFwaIG3/0qSnwfz8fIuL8nvGAhUPBbgWbtK3qTsif5\nCCvahuWrUH2WHGMPvQIDAQAB\n-----END PUBLIC KEY-----'  # noqa: E501
A = vehicle.Vehicle(
    'Ford', 'Focus', 2021, '9f7h4sqc', A_private_key, A_public_key
)
A_pub_identity = A.encodeIdentity()
print(f'A public identity: {A_pub_identity}')

""" Vehicle B generates its own digital identity using its public data and
private key. """
B_private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQC7gH9GHz+fMSWE1g1Zvmz8JMdaNUt05nmmRdGwztFr24YFQcdz\nZOB0pCxHk1TfnTJP/08lF5NGxYqmK7KDs5yt7stNAYWr19oBld6Y98bRXHpa2Yyn\nPy3Ic1LTjbgezLepwPGlemxlcaUQaEcGQRGlwIq3zKNb9Nxuc44mEw45ZwIDAQAB\nAoGATg9M7VCNGCVJzWef30Db9o0JQZD2fRCGjKZ8ifNQVGrr/LxJ4MyadXTzykiY\nCRBUpeFQfcy2z7vl4RBIHXRlQX23hHksfeoX3mE7xqLbtp0BUrnBgjCrXSxKF+eA\nNngnEmonPgGDUIvoJFaAuJFhI0WE4RCOwZtLqErQPKZqyGECQQDfYbcotPdJt7Yt\nF7Ov8n+aDU+Fb+jK3ET7bIP3kPybxpe3a7axMaUhPNKE5M1l3CYUFKm1ofhwqrKI\n143nLdR9AkEA1uGNSIlUYEqsdFqU+grzb9umrbwG1N8Z7xsAt/ejXrcZKBhz8IMh\nJtqPMYN7wS8TJWwymB1BCyT6MgR6AkweswJBAJue/rP8Rt7zfpYxkfw8y8quBT1n\n9l0FUYV7VwCs4F9B3kZpYxBVDr52Gg99Ot8AnQKWVpj0KxmKwfB1gyWQFx0CQQCM\nY/zswVyxNNiLhIsE+pamJHo31DsaZVEKWTgU+eRxA2uaOK+3GdVVD0Ky9NasFteJ\ngbFklOhkIZqdhzM3wQflAkBHCjL5DxxQzTmv91Erx0N3kzJL0a1sj/4Yyt2fh6gO\nbXprRKrbQ6GNPapf81Lg/mO9qYSeseqK6V5dzl4UrAmI\n-----END RSA PRIVATE KEY-----'  # noqa: E501
B_public_key = b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC7gH9GHz+fMSWE1g1Zvmz8JMda\nNUt05nmmRdGwztFr24YFQcdzZOB0pCxHk1TfnTJP/08lF5NGxYqmK7KDs5yt7stN\nAYWr19oBld6Y98bRXHpa2YynPy3Ic1LTjbgezLepwPGlemxlcaUQaEcGQRGlwIq3\nzKNb9Nxuc44mEw45ZwIDAQAB\n-----END PUBLIC KEY-----'  # noqa: E501
B = vehicle.Vehicle(
    'Tesla', 'Model S', 2020, 'a305d39e', B_private_key, B_public_key
)
B_pub_identity = B.encodeIdentity()
print(f'B public identity: {B_pub_identity}')

# PKG takes action.
PKG = CocksPKG(2048)

""" 1. Vehicle A asks the PKG for the public data of vehicle B. """
pkg_private_key, pkg_public_hashed_identity = PKG.extract(
    B_pub_identity.decode()
)
pkg_public_modulus = PKG.n

""" 2. PKG, which has the public key of A (and of all vehicles), verifies the
identity signature of vehicle A using A_pub_identity. """
try:
    jwt.decode(A_pub_identity, A_public_key, algorithms=['RS256'])
except Exception as e:
    print(f'ERROR: {e}')
    sys.exit(1)

""" 3. If the previous verification was successful, PKG returns to vehicle A
only vehicle B's pkg_public_hashed_identity and pkg_public_modulus. """
print(f'pkg_public_hashed_identity: {pkg_public_hashed_identity}')
print(f'pkg_public_modulus: {pkg_public_modulus}')

""" 4. Vehicle A encrypts the message using vehicle B's pkg_public_modulus,
B_pub_identity, and pkg_public_hashed_identity. """
cocks = Cocks(pkg_public_modulus)
encrypted_msg = cocks.encrypt(b'Hola mundo!', pkg_public_hashed_identity)

""" 5. Vehicle A sends the encrypted message to vehicle B. """
print(f'encrypted_msg: {encrypted_msg}')

""" 6. Vehicle B asks the PKG for its pkg_private_key and
pkg_public_hashed_identity. """
print(f'pkg_private_key: {pkg_private_key}')

""" 7. PKG, which has the public key of B (and of all vehicles), verifies the
identity signature of vehicle B using B_pub_identity. """
try:
    jwt.decode(B_pub_identity, B_public_key, algorithms=['RS256'])
except Exception as e:
    print(f'ERROR: {e}')
    sys.exit(1)

""" 8. Vehicle B decrypts the encrypted message sent to it by vehicle A using
pkg_private_key and pkg_public_hashed_identity. """
decrypted_msg = cocks.decrypt(
    encrypted_msg,
    pkg_private_key,
    pkg_public_hashed_identity
).decode()
print(f'decrypted_msg: {decrypted_msg}')
