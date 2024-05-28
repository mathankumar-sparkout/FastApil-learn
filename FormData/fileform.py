from fastapi import FastAPI,File,Form,UploadFile
from typing import Annotated
app=FastAPI()

@app.post("/FileForm")
async def fileform(file:Annotated[bytes,File()]=None,
                   form:Annotated[str,Form()]=None,
                   uploadfile:Annotated[UploadFile,None]=None):
    return {"file":len(file),"uploadfile":uploadfile.filename,"form":form}
"""
overall added the file,form,upload method 
use in function
"""
