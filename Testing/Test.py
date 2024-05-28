from fastapi import FastAPI
from fastapi.testclient import TestClient #import test cilent

app=FastAPI()

@app.get("/")
async def fun():
    return{"msg:hello word"} # return msg 

test=TestClient(app) #store the testclient in test variable

def fun1():
    response=test.get("/")   
    assert response.status_code ==200  # view this status code
    assert response.json()=={"msg :Hello word"} # view the msg 
    
