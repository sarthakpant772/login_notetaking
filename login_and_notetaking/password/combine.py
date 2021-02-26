from login_sinup import check
num=int(input("if you want to log in enter 1 \n if you want to signup enter 2\n"))
rad=check(num)
if(num==1):
    rad.login()
else:
    rad.signup()    