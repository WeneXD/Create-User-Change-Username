from pydantic import BaseModel
from b64 import b64
import re

class User(BaseModel):
    name: str
    pw: str
    def change_name(self,name,token):
        if len(name)!=len(re.sub(r"[^a-zA-Z0-9]","",name)):
            return {"out":False,"na":name,"err":"Name contains invalid characters"}
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
    if None in [_name,_pw]:
        return {"out":False,"na":_name,"err":"Value missing"}
    if len(_name)!=len(re.sub(r"[^a-zA-Z0-9]","",_name)):
        return {"out":False,"na":_name,"err":"Name contains invalid characters"}
    if len(_pw)!=len(re.sub(r'[^a-zA-Z0-9\-\_\.]',"",_pw)):
        return {"out":False,"na":_name,"err":"Password contains invalid characters"}
    for us in user.values():
        if _name==us.name:
            return {"out":False,"na":_name,"err":"Name is already taken"}
    if None in [_name,_pw]:
        return {"out":False,"na":_name,"err":"Value missing"}
    user[len(user)+1]=User(name=_name,pw=_pw)
    return {"out":True,"na":_name,"token":b64("enc",_name+_pw)}

def change_name(name,token):
    if None in [name,token]:
        return {"out":False,"na":name,"err":"Value missing"}
    id=-1
    for _id, us in user.items():
        if token==b64("enc",us.name+us.pw):
            id=_id
            break
    if id==-1:
        return {"out": False,"na":name,"err":"User not found/Invalid Token"}
    else:
        return user[id].change_name(name,token)
