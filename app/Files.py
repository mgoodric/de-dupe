class Files:

    @staticmethod
    def add(database, path_hash, path, file_name, file_hash):
        sql = ("INSERT INTO files "
               "(path_hash, path, file_name, file_hash) "
               "VALUES (%s, %s, %s, %s)")
        sql_vars = (path_hash, path, file_name, file_hash)

        try:
            database.execute(sql, sql_vars)
            database.commit()
            return True
        except Exception as err:
            print("Something went wrong: {}".format(err))
            return False