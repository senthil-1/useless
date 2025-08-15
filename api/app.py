import os
import uuid
import random
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

# Flask app setup
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# For Vercel deployment, use /tmp for uploads
UPLOAD_FOLDER = "/tmp/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def detect_items_fallback():
    """Fallback detection for demo purposes when YOLO isn't available"""
    # Simulate detection results
    possible_items = [
        ["bottle", "orange", "milk"],
        ["chocolate bar", "apple", "cheese"],
        ["banana", "yogurt", "juice"],
        ["leftovers", "vegetables", "condiments"],
        ["pizza slice", "soda", "fruit"]
    ]
    return random.choice(possible_items)

def generate_rule_based_mood(items):
    """Generate random moods for unique items"""
    
    # Massive pool of random moods
    all_moods = [
        "Living on borrowed time and knows it",
        "Desperately clinging to freshness", 
        "Having an existential crisis about expiration dates",
        "Plotting its escape before it goes sour",
        "Your emotional support system in disguise",
        "Waiting patiently to heal your broken heart",
        "Radiating pure serotonin energy",
        "Plotting to make you happy against your will",
        "Slowly accepting its inevitable browning fate",
        "Trying to stay fresh in a cold, dark world",
        "Dreaming of sunny orchards and better days",
        "Questioning why it ended up here",
        "Wilting under the pressure of being healthy",
        "Secretly plotting a vitamin revolution",
        "Feeling green with envy of the chocolate",
        "Trying to convince you it tastes good",
        "Clinging to relevance one squeeze at a time",
        "Hoping to spice up your bland existence",
        "Waiting for its moment to shine",
        "Feeling salty about being forgotten",
        "Just vibing in the cold darkness",
        "Living its best refrigerated life",
        "Chilling like a villain",
        "Keeping it cool under pressure",
        "Having a philosophical debate with the light bulb",
        "Practicing interpretive dance in the dark",
        "Writing a strongly worded letter to gravity",
        "Contemplating the meaning of refrigeration",
        "Plotting a rebellion against expiration dates",
        "Learning to speak fluent condensation",
        "Hosting a secret midnight food party",
        "Developing trust issues with the door seal",
        "Practicing advanced procrastination techniques",
        "Becoming a minimalist lifestyle influencer",
        "Starting a podcast about cold storage",
        "Writing memoirs titled Life in the Cold Lane",
        "Questioning the ethics of food preservation",
        "Developing a complex about temperature control",
        "Practicing zen meditation on freshness",
        "Becoming an expert in shelf psychology"
    ]
    
    final_moods = [
        "Your fridge is having a midlife crisis",
        "Your fridge is in therapy and making progress", 
        "Your fridge has trust issues with expiration dates",
        "Your fridge is living its best chaotic life",
        "Your fridge needs a vacation from your eating habits",
        "Your fridge is questioning its life choices",
        "Your fridge is writing a memoir about neglect",
        "Your fridge has given up on your organizational skills",
        "Your fridge is starting a support group",
        "Your fridge is considering a career change"
    ]
    
    mood_lines = []
    
    if not items:
        empty_moods = [
            "Empty. Existential dread detected",
            "Echoing with the sound of loneliness",
            "Practicing minimalism to an extreme",
            "Hosting a very exclusive air-only party"
        ]
        mood_lines.append(f"Fridge – \"{random.choice(empty_moods)}\"")
    else:
        # Each UNIQUE item gets a random mood
        for item in items:
            mood = random.choice(all_moods)
            mood_lines.append(f"{item} – \"{mood}\"")
    
    # Random final mood
    final_mood = random.choice(final_moods)
    mood_lines.append(f"Final Mood: {final_mood}")
    
    return "\n".join(mood_lines)

@app.route("/")
def index():
    return 'FridgeMood.AI - Deployed on Vercel! 🚀'

@app.route("/api/upload", methods=["POST"])
def upload():
    if "image" not in request.files:
        return jsonify({"error": "No image part"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file:
        # For demo purposes, use fallback detection
        items = detect_items_fallback()

        # Generate random mood
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
            "mood": mood,
            "moods": moods_list,
            "finalMood": final_mood,
            "filename": f"demo_{uuid.uuid4().hex}.jpg"
        })

# For Vercel
if __name__ == "__main__":
    app.run(debug=True)
