import jwt
# Doc: https://pyjwt.readthedocs.io/en/latest/usage.html


class Vehicle:
    def __init__(
        self, brand, model, year, frameNumber, private_key, public_key
    ):
        self.brand = brand
        self.model = model
        self.year = year
        self.frameNumber = frameNumber
        self.__private_key = private_key
        self.public_key = public_key

    def encodeIdentity(self):
        data = {
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'frameNumber': self.frameNumber
        }
        return jwt.encode(data, self.__private_key, algorithm='RS256')
