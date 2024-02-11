  
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import os
app = FastAPI()

UPLOAD_FOLDER = "uploaded_images"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

html_form = """
<h1 align="center"> Plant disease Detection</h1>
<form action="/uploadfile/" enctype="multipart/form-data" method="post">

<div align="center">
    <input type="file" name="file" accept="image/*">
    <input type="submit" value="Upload Image">
   </div> 
    <div>
    <p> This is .....</p>
    </div>
</form>
"""

@app.get("/", response_class=HTMLResponse)
async def main():
    return HTMLResponse(content=html_form, status_code=200)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as image_file:
        image_file.write(file.file.read())
    return {"filename": file.filename, "file_path": file_path}


