from fastapi import FastAPI, Request, HTTPException
from notebooklm_py import NotebookLM
import os

app = FastAPI()

# سطر إضافي للتأكد أن السيرفر شغال إذا فتحت الرابط في المتصفح
@app.get("/")
async def root():
    return {"message": "Server is Running!"}

@app.post("/upload")
async def upload_to_notebook(request: Request):
    data = await request.json()

    # البيانات القادمة من n8n
    nb_id = data.get("notebook_id")
    title = data.get("title")
    content = data.get("content")

    # تأمين بسيط: التأكد من وجود البيانات
    if not nb_id or not content:
        raise HTTPException(status_code=400, detail="Missing notebook_id or content")

    try:
        # تصحيح اسم المتغير ليطابق ما وضعته في Render
        cookies = os.getenv("NB_COOKIES")
        if not cookies:
            raise Exception("NB_COOKIES not found in environment variables")

        nlm = NotebookLM(cookies=cookies)
        notebook = nlm.get_notebook(nb_id)

        # إضافة النص كمصدر
        notebook.add_source(title=title, content=content)

        return {"status": "Success", "details": "Uploaded to NotebookLM"}
    except Exception as e:
        print(f"Error: {str(e)}") # سيظهر هذا في الـ Logs عندك
        raise HTTPException(status_code=500, detail=str(e))
