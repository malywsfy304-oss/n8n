from fastapi import FastAPI, Request, HTTPException
from notebooklm_py import NotebookLM
import os

app = FastAPI()

@app.post("/upload")
async def upload_to_notebook(request: Request):
    data = await request.json()

    # البيانات القادمة من n8n
    nb_id = data.get("notebook_id")
    title = data.get("title")
    content = data.get("content")

    try:
        # استخدام الكوكيز المخزنة في السيرفر لتسجيل الدخول
        nlm = NotebookLM(cookies=os.getenv("MY_COOKIES"))
        notebook = nlm.get_notebook(nb_id)

        # العملية السحرية: إضافة النص كمصدر
        notebook.add_source(title=title, content=content)

        return {"status": "Success", "details": "Uploaded to NotebookLM"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
