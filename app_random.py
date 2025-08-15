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
# Random mood generator with lots of variety
# --------------------------
def generate_random_mood(items):
    """Generate random, humorous moods for fridge items"""
    
    # Mood templates for different item categories
    mood_templates = {
        'milk': [
            "Living on borrowed time and knows it",
            "Desperately clinging to freshness",
            "Having an existential crisis about expiration dates",
            "Plotting its escape before it goes sour",
            "Wondering if it's still the chosen one",
            "Feeling udderly confused about its purpose",
            "Contemplating the meaning of pasteurization",
            "Secretly judging your cereal choices",
            "Dreaming of being chocolate milk when it grows up",
            "Questioning the ethics of calcium supplements"
        ],
        'chocolate': [
            "Your emotional support system in disguise",
            "Waiting patiently to heal your broken heart",
            "Radiating pure serotonin energy",
            "Plotting to make you happy against your will",
            "Silently judging your diet choices",
            "Being the hero you don't deserve",
            "Melting with anticipation",
            "Whispering sweet nothings about dopamine",
            "Practicing mindful meditation on sweetness",
            "Plotting world domination through endorphins"
        ],
        'fruit': [
            "Slowly accepting its inevitable browning fate",
            "Trying to stay fresh in a cold, dark world",
            "Dreaming of sunny orchards and better days",
            "Questioning why it ended up here",
            "Competing in a silent beauty contest",
            "Hoping to avoid the compost bin",
            "Living its best vitamin-packed life",
            "Photosynthesizing nostalgic memories",
            "Writing poetry about seasonal depression",
            "Contemplating the circle of life"
        ],
        'vegetable': [
            "Wilting under the pressure of being healthy",
            "Secretly plotting a vitamin revolution",
            "Feeling green with envy of the chocolate",
            "Trying to convince you it tastes good",
            "Having a root awakening about life",
            "Leafing through its options",
            "Staying grounded despite the circumstances",
            "Branching out into new flavor territories",
            "Practicing photosynthesis meditation",
            "Organizing a fiber support group"
        ],
        'condiment': [
            "Clinging to relevance one squeeze at a time",
            "Hoping to spice up your bland existence",
            "Waiting for its moment to shine",
            "Feeling salty about being forgotten",
            "Preserving itself for better times",
            "Adding flavor to an otherwise boring shelf life",
            "Bottling up its emotions",
            "Seasoning its words carefully",
            "Marinating in existential thoughts",
            "Fermenting philosophical ideas"
        ],
        'generic': [
            "Just vibing in the cold darkness",
            "Living its best refrigerated life",
            "Chilling like a villain",
            "Keeping it cool under pressure",
            "Frozen in time and space",
            "Having a cool relationship with temperature",
            "Maintaining its composure in the cold",
            "Embracing the minimalist lifestyle",
            "Practicing zen refrigeration",
            "Meditating on the meaning of preservation"
        ]
    }
    
    # Final mood options
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
        "Your fridge is considering a career change",
        "Your fridge is practicing mindfulness meditation",
        "Your fridge has developed commitment issues",
        "Your fridge is going through an identity crisis",
        "Your fridge is contemplating early retirement",
        "Your fridge has joined a self-help book club",
        "Your fridge is learning to love itself",
        "Your fridge is taking up yoga and essential oils",
        "Your fridge is writing angry letters to food manufacturers"
    ]
    
    mood_lines = []
    
    if not items:
        empty_moods = [
            "Empty. Existential dread detected",
            "Echoing with the sound of loneliness",
            "Practicing minimalism to an extreme",
            "Hosting a very exclusive air-only party",
            "Living the Marie Kondo dream",
            "Embracing the void with open shelves",
            "Meditating on the concept of nothingness",
            "Achieving peak zen through emptiness",
            "Becoming one with the cosmic void",
            "Practicing advanced minimalist philosophy"
        ]
        mood_lines.append(f"Fridge – \"{random.choice(empty_moods)}\"")
    else:
        # Create a pool of ALL possible moods for maximum randomness
        all_moods = []
        for category_moods in mood_templates.values():
            all_moods.extend(category_moods)

        # Add some extra wild and random moods
        extra_wild_moods = [
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
            "Writing memoirs titled 'Life in the Cold Lane'",
            "Questioning the ethics of food preservation",
            "Developing a complex about temperature control",
            "Practicing zen meditation on freshness",
            "Becoming an expert in shelf psychology",
            "Writing angry reviews about your eating habits",
            "Contemplating early retirement to a compost bin",
            "Learning advanced techniques in staying cool",
            "Developing separation anxiety from other foods"
        ]

        all_moods.extend(extra_wild_moods)

        # Assign completely random moods to each item
        for item in items:
            # Each item gets a completely random mood from the entire pool
            mood = random.choice(all_moods)
            mood_lines.append(f"{item} – \"{mood}\"")
    
    # Add random final mood
    final_mood = random.choice(final_moods)
    mood_lines.append(f"Final Mood: {final_mood}")
    
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

        # Generate random mood
        mood = generate_random_mood(items)

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

@app.route('/')
def index():
    return 'FridgeMood.AI Backend with Random Moods is running!'

if __name__ == "__main__":
    print("Starting FridgeMood.AI backend with random moods...")
    app.run(debug=True, host='127.0.0.1', port=5000)
