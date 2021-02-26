userName=open("user_Name.txt",'a')
userPass=open("user_password.txt",'a')

class password:
    def __init__(self,user_name,passw):
        self.user_name=user_name 
        self.passw=passw

    def save(self):
        userName.write("username "+self.user_name+" ")
        userName.write("password "+self.passw+" ")
