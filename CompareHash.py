improt sys
import os
import hashlib

from ClassificationOfFile import DefineDirs


class Hashing:
        def hash_compare (self,path):
                hasherFirst = hashlib.md5()
                open_first = open(self,'rb')
                read_first = open_first.read()
                update_first = hasherFirst.update(read_first)
                hash_of_first = (str((hasherFirst.hexdigest())))

                hasherSecond = hashlib.md5()
                open_second = open(path,'rb')
                read_second = open_second.read()
                update_second = hasherSecond.update(read_second)
                hash_of_second = (str(hasherSecond.hexdigest()))

                # Comparing MD5 hash of two files.
                if hash_of_first == hash_of_second :
                    print("Both the files are same")
                else:
                    print("Both the files are different")


dirs = DefineDirs()
