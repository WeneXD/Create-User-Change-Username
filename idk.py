import requests as re
from subprocess import call

def clr(): call("cls",shell=True)

ip="localhost"
port="8000"
addr=f'http://{ip}:{port}'
token=""
def main():
    clr()
    print("[reg]\t\tRegister\n[chName]\tChange Name\n[users]\t\tUserlist\n[spamreg]\t\tSpam register 50 users")
    print(f'Token: {token}')
    x=input(">").lower()
    if x in ["reg","chname","users","spamreg"]:
        globals()[x]()
    main()

def reg():
    clr()
    user={'name':input('Name: '),'password':input('Password: ')}
    resp=re.post(addr+"/register/?name="+f"{user['name']}&pw={user['password']}")
    meow=resp.json()
    clr()
    if 'err' in meow:
        print("User not created\n")
        print(f"Error: {meow['err']}")
        input()
        return
    print("\nUser created\n")
    print(f"Name: {meow['na']}\nToken: {meow['token']}")
    globals()['token']=meow['token']
    input()

def spamreg():
    for x in range(50):
        re.post(addr+f"/register/?name={x}&pw={x}")

def chname():
    clr()
    user={'name':input('New Name: '),token:""}
    user['token']=globals()['token']
    if user['token']=="":
        user['token']=input("Token: ")
    resp=re.post(addr+'/change_name/?newName='+f"{user['name']}&token={user['token']}")
    meow=resp.json()
    clr()
    if 'err' in meow:
        print("Username not changed\n")
        print(f"Error: {meow['err']}")
        input()
        return
    print("\nUsername changed\n")
    print(f"New Name: {user['name']}\nNew Token: {user['token']}")
    globals()['token']=user['token']
    input()

def users():
    clr()
    print("USERS\n")
    resp=re.get(addr+'/userlist/')
    meow=resp.json()
    if not meow:
        print("No Users")
        input()
        return
    users={}
    for id,us in meow.items():
        print(f"ID: {id}\t\t{us['name']}")
    input()

main()