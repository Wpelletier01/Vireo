
import bcrypt
 
# Declaring our password
password = b'ssdfsdafsfghhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhgggggggggggggg'
 
# Adding the salt to password
salt = bcrypt.gensalt(rounds=10)
# Hashing the password



hashed = bcrypt.hashpw(password, salt)
print(salt)
print(hashed)
