import mysql.connector
import os
from DirectoryUtils import DirectoryUtils
from HashUtils import HashUtils
from Files import Files
from Database import Database

DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')
DB_SCHEMA = os.environ.get('DB_SCHEMA')

paths = ["/Dropbox"]

with Database(DB_USER, DB_PASS, DB_NAME, DB_SCHEMA) as db:
    for p in paths:
        for root, dirs, files in os.walk(p):
            print(root)
            path = root.split(os.sep)
            print((len(path) - 1) * '---', os.path.basename(root))
            for file in files:
                print(len(path) * '---', file)
                file_name = file
                print(file_name)
                full_path = os.path.join(root, file)
                print(full_path)
                path_hash = HashUtils.hash_sha256_hex(full_path)
                print(path_hash)
                with open(full_path, "rb") as f:
                    bytes = f.read()
                    file_hash = HashUtils.hash_sha256_hex(bytes)
                    print(file_hash)
                    add_result = Files.add(db, path_hash, full_path, file_name, file_hash)
                    print(add_result)