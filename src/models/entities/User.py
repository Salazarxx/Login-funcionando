from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, username, password, fullname="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname
       

    @classmethod
    def check_password(self, hashed_password, password):
         #print(hashed_password) 
         #print(password)        
         return check_password_hash(hashed_password, password)

#print(generate_password_hash("123456"))
password="Panter.479"
pbkdpass="scrypt:32768:8:1$2fdQhSpm5fDNLIbx$fac93b827babf982c0a9e743dbd9f17bddf31056d266b57c3b7554ff61a467f1522a221b0962ebfc67ce3e780d23fdb6beeb9db35e70d2a51b11387a2c86509d"
pbkdpass2="pbkdf2:sha256:260000$fiRyeVmApEki8uvm$40d93cdea3f941010f3eedfafd228db15c41810ce625a691ff8cb2491300b010"
# Example usage: Hashing a password
password = "Panter.479"
hashed_password = generate_password_hash(password,method='pbkdf2:sha256:260000')
print(f"Hashed Password: {hashed_password}")

# Example usage: Verifying a password
is_valid = check_password_hash(pbkdpass, password)
print(f"Password is valid: {is_valid}")

#other check

is_valid = check_password_hash(pbkdpass2, "suscribete")
print(f"Password is valid: {is_valid}")