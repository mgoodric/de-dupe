import mysql.connector
from DirectoryUtils import DirectoryUtils
from HashUtils import HashUtils
from Files import Files
from Database import Database

result = DirectoryUtils.scan_directory("/Users/matthew.goodrich/Downloads")

with Database('root', 'example', '127.0.0.1', 'fileinfo') as db:
    for r in result:
        if r.is_dir():
            break
        file_name = r.name
        full_path = str(r.resolve())
        path_hash = HashUtils.hash_sha256_hex(full_path)
        with open(full_path, "rb") as f:
            bytes = f.read()
            file_hash = HashUtils.hash_sha256_hex(bytes)
            print(file_name)
            print(file_hash)
            print(full_path)
            print(path_hash)
            add_result = Files.add(db, path_hash, full_path, file_name, file_hash)
            print(add_result)