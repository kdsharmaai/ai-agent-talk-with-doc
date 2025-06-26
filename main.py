from dotenv import load_dotenv
from graph import graph
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

load_dotenv()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/uploads", methods=["POST"])
def uploads():
    # Upload the file in "uploads" and return JSON response like { "success": true } or { "success": false, "error": "reason" }.
    if 'file' not in request.files:
        return jsonify({"success": False, "error": "No file part in the request."}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"success": False, "error": "No file selected."}), 400
    if not file.filename.lower().endswith('.pdf'):
        return jsonify({"success": False, "error": "Only PDF files are allowed."}), 400
    file.seek(0, 2)  # Seek to end to get size
    file_length = file.tell()
    file.seek(0)  # Reset pointer
    if file_length > 500 * 1024:
        return jsonify({"success": False, "error": "File size must be less than 500 KB."}), 400
    upload_folder = os.path.join(os.path.dirname(__file__), 'uploads')
    os.makedirs(upload_folder, exist_ok=True)
    save_path = os.path.join(upload_folder, file.filename)
    try:
        file.save(save_path)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
    
@app.route("/api/process", methods=["POST"])
def process():
    # Get uploaded file name here
    user_input = request.json.get("question", "")
    file_name = request.json.get("file_name", "")
    if not file_name:
        return jsonify({"output": "No file uploaded.", "success": False}), 400
    data = {
        "messages": [
            {"role": "user", "content": f"uploads/{file_name}"},  # PDF upload
            {"role": "user", "content": f"{user_input}"}  # User question
        ],
        "pdf_content": ""
    }
    result = graph.invoke(data)
    return jsonify({"output": result['messages'][-1].content, "success": True})

if __name__ == "__main__":
    app.run(debug=True, port=5002)