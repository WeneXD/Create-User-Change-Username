from pydantic import BaseModel
from b64 import b64
class User(BaseModel):
    name: str
    pw: str
    def change_name(self,name,token):
        if name==self.name:
            return {"out": False,"na":name,"err":"Name is already: "+name}
        for us in user.values():
            if name==us.name:
                return {"out": False, "na":name,"err":"Name is taken"}
        print(f"\t{self.name}->{name}")
        self.name=name
        return {"out": True,"na":self.name,"token":b64("enc",self.name+self.pw)}

user={}

def create_user(_name,_pw):
    for us in user.values():
        if _name==us.name:
            return {"out":False,"na":_name,"err":"Name is already taken"}
    user[len(user)+1]=User(name=_name,pw=_pw)
    return {"out":True,"na":_name,"token":b64("enc",_name+_pw)}

def change_name(name,token):
    id=-1
    for _id, us in user.items():
        if token==b64("enc",us.name+us.pw):
            id=_id
            break
    if id==-1:
        return {"out": False,"na":name,"err":"User not found/Invalid Token"}
    else:
        return user[id].change_name(name,token)
