import sys
import os
import glob
import hashlib


def md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(2 ** 20), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()




