import user as u
from user import user
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return ":-D"

@app.post("/register/")
def register(name:str | None=None, pw:str | None=None):
    print("\n\t[Registering User]")
    meow=u.create_user(name,pw)
    print(f"\tUser registered: {meow['out']} ({meow['na']})")
    if "err" in meow:
        print(f"\tError: {meow['err']}")
    return meow

@app.post("/change_name/")
def change_name(newName:str | None=None,token:str | None=None):
    print("\t[Changing username]")
    meow=u.change_name(newName,token)
    print(f"\tUsername changed:{meow['out']} ({meow['na']})")
    if "err" in meow:
        print(f"\tError: {meow['err']}")
    return meow

@app.get("/userlist/")
def get_userlist():
    print("\n\t[Printing userlist]")
    return user

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="localhost", port=8000)
