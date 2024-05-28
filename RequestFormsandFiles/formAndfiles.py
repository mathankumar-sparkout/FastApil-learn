from fastapi import FastAPI,File,UploadFile,Form
from typing import Annotated




app=FastAPI()

@app.post("/root")
async def fun(file:Annotated[bytes,File()],fileb:Annotated[UploadFile,File()],token:Annotated[str,Form()]):
    return {"file":len(file),"filelub":fileb,"token":token}  
  