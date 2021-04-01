import logging
import json
from dataclasses import dataclass


@dataclass
class FacebookCredentials:
    email: str = ""
    password: str = ""
    username: str = ""

    def keys(self):
        return self.__dict__.keys()

    def __getitem__(self, item):
        return getattr(self, item)

    @classmethod
    def from_dict(cls, **dictionary):
        return cls(**dictionary)

    @classmethod
    def from_jsonfile(cls, file):
        with open(file) as fp:
            dictionary = json.load(fp)
        return FacebookCredentials.from_dict(**dictionary)

    @classmethod
    def from_json(cls, jsonstring):
        dictionary = json.loads(jsonstring)
        return FacebookCredentials.from_dict(**dictionary)


if __name__ == '__main__':
    credentials = FacebookCredentials.from_jsonfile("../myob/facebook.json")
    print(credentials)

    credentials.email = "nomail"
    print(credentials)

    def test_unpack(email, password, username):
        print(email, password, username)

    test_unpack(**credentials)