from fastapi import FastAPI, File, UploadFile  # file,uploadfile import fastapi
from typing import Annotated, Union


app = FastAPI()


@app.post("/file")
async def fun(file: Annotated[bytes, File()]):  # file (query parameter)
    return {"file": len(file)}  # return file len


@app.post("/upload file")
async def fun(file: UploadFile):
    return {"uploadfile": file.filename}  # return file.filename (ex:requestfile.py)

#-----------------------------------------------------------------------------------------------------------------------
@app.post("/file len")
async def fun(file: Annotated[Union[bytes, None], File()] = None): #optional used this statement
    if not File:
        return {"file not found"} #  not in file throw error msg
    else:
        return {"file len": len(file)} # return file lenth


@app.post("/file_upload")
async def fun(file: UploadFile):
    if not File:
        return {"file not upload"} #not in file throw error msg
    else:
        return {"file_upload": file.filename} #return file.filename
    
    
#------------------------------------------------------------------------------------------------------------------------


@app.post("/files")
async def fun(file:Annotated[bytes,File(description="A file read as bytes")]):
    return {"file_len":len(file)}

@app.post("/UploadFiles")
async def fun(file:Annotated[UploadFile,File(description="A file read as bytes")]):
    return {"upload files":file.filename}




from typing import Annotated

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/files/")
async def create_files(files: Annotated[list[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}