#
# Keep this file if I need to recreate the database
#




def _create_default_user(self):

    data = pd.read_csv("src/userinfov2.csv")
    x = 1
    for _,row in data.iterrows():

        print(row)

        middle = None
        if row["mname"] != "":
            middle = row["mname"]

            create = f""" 
                INSERT INTO accountIds (
                    id,
	                username,
                    password
                )
                VALUES 
                ( {x},'{row["username"]}',"{row["passwd"]}")

            """

            create2 = f"""

            INSERT INTO accountInfo (
		        id,
	            fname,
                mname,
                lname,
                email,
                birth

            )   
            VALUES
            ({x},'{row["fname"]}','{middle}','{row["lname"]}','{row["email"]}',Date('{row["bday"]}'));
            
            """

            self._cursor.execute(create)

            self._connection.commit()

            self._cursor.execute(create2)

            self._connection.commit()
            x += 1
