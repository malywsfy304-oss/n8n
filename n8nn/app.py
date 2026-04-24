

# import json
# import requests
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # 1. تحميل الكوكيز من الملف الخارجي
# def get_session():
#     session = requests.Session()
#     try:
#         with open('cookies.json', 'r') as f:
#             cookies_dict = json.load(f)
#             for name, value in cookies_dict.items():
#                 session.cookies.set(name, value)
#         return session
#     except Exception as e:
#         print(f"Error loading cookies: {e}")
#         return None

# # 2. صفحة رئيسية للتأكد أن السيرفر يعمل
# @app.route('/', methods=['GET'])
# def home():
#     return jsonify({"status": "online", "message": "خادم الخوارزمي يعمل بنجاح"})

# # 3. نقطة استلام الملفات من n8n
# @app.route('/upload-from-n8n', methods=['POST'])
# def handle_n8n_upload():
#     if 'file' not in request.files:
#         return jsonify({"error": "No file part"}), 400
    
#     file = request.files['file']
#     notebook_id = request.form.get('notebook_id')

#     session = get_session()
#     if not session:
#         return jsonify({"error": "Session failed"}), 500

#     UPLOAD_URL = f"https://notebooklm.google.com/api/v1/notebooks/{notebook_id}/sources"

#     files = {
#         'file': (file.filename, file.read(), 'application/pdf')
#     }

#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#         "Referer": "https://notebooklm.google.com/"
#     }

#     try:
#         response = session.post(UPLOAD_URL, headers=headers, files=files)
#         if response.status_code == 200:
#             return jsonify({"status": "Success", "data": response.json()})
#         else:
#             return jsonify({"status": "Failed", "code": response.status_code, "msg": response.text})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500




# # تصحيح مكان تشغيل السيرفر (يجب أن يكون في بداية السطر)
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=7860)


import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.get_json(silent=True) or request.form.to_dict()
        return jsonify({
            "status": "success", 
            "msg": "تم الاتصال بنجاح من Render", 
            "data": content
        })
    return "سيرفر محمد يعمل الآن على Render بنجاح!"

if __name__ == "__main__":
    # هذا السطر هو الأهم: Render هو من يحدد المنفذ (Port)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
