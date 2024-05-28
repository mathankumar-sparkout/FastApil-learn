from fastapi import FastAPI,File,UploadFile
from typing import Annotated,Union
from fastapi.responses import HTMLResponse
app=FastAPI()

@app.post("/File")
async def file(file: Annotated[Union[bytes, None], File(description="A file read as bytes")] = None):
    if not file:
        return{"message:No file"}
    return{"file":len(file)}
"""
file :annotated union bytes are None ,file description display
there is no file throw the meassage
otherwise return lenth of file
"""

@app.post("/uploadFile")
async def uploadfile(file:Annotated[UploadFile,None]=None):
    if not file:
        return{"message:no file uploaded"}
    return{"file":file.filename}
"""
file upload or none file upload
no file upload throw the message
otherwise return the file and filename
"""


@app.post("/uploadfiles")
async def uploadfiles(files:Annotated[list[UploadFile],File(description="upload file")]):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)