import os
import uuid
import random
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from ultralytics import YOLO
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask app setup
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load YOLO model (change to your model path if needed)
model = YOLO("yolov8n.pt")

# --------------------------
# Detection function
# --------------------------
def detect_items(image_path):
    results = model(image_path)
    detected_items = []
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            detected_items.append(label)
    return detected_items

# --------------------------
# Offline rule-based mood generator
# --------------------------
def generate_rule_based_mood(items):
    mood_lines = []
    if not items:
        mood_lines.append("Fridge – \"Empty. Existential dread detected.\"")
    else:
        for item in items:
            if "milk" in item.lower():
                mood_lines.append(f"{item} – \"Toxic. Let it go.\"")
            elif "chocolate" in item.lower():
                mood_lines.append(f"{item} – \"Emotional support system detected.\"")
            elif "lemon" in item.lower():
                mood_lines.append(f"{item} – \"Fighting for survival.\"")
            elif "ketchup" in item.lower():
                mood_lines.append(f"{item} – \"Clings to the past. Hopes you’ll order fries.\"")
            elif "curd" in item.lower():
                mood_lines.append(f"{item} – \"In a committed but confusing relationship.\"")
            else:
                mood_lines.append(f"{item} – \"Just vibing in here.\"")
    mood_lines.append("Final Mood: Your fridge is in a midlife crisis.")
    return "\n".join(mood_lines)

# --------------------------
# Upload route
# --------------------------
@app.route("/upload", methods=["POST"])
def upload():
    if "image" not in request.files:
        return jsonify({"error": "No image part"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file:
        filename = secure_filename(file.filename)
        unique_name = f"{uuid.uuid4().hex}{os.path.splitext(filename)[1]}"
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], unique_name)
        file.save(file_path)

        # Detect items
        items = detect_items(file_path)

        # Generate offline mood
        mood = generate_rule_based_mood(items)

        # Format structured JSON
        moods_list = []
        final_mood = ""
        for line in mood.split("\n"):
            if line.strip():
                if line.lower().startswith("final mood:"):
                    final_mood = line.replace("Final Mood:", "").strip()
                else:
                    try:
                        name, mood_text = line.split(" – ", 1)
                        moods_list.append({
                            "name": name.strip(),
                            "mood": mood_text.strip().strip('"')
                        })
                    except ValueError:
                        pass

        return jsonify({
            "mood": mood,  # Original format for backward compatibility
            "moods": moods_list,  # New structured format
            "finalMood": final_mood,
            "filename": unique_name
        })

if __name__ == "__main__":
    app.run(debug=True)
