from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import uuid
import random
from ultralytics import YOLO

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load YOLO model
model = YOLO("yolov8n.pt")

# Item mapping for better fridge context
def map_to_fridge_items(detected_label):
    """Map YOLO detected items to more appropriate fridge items"""

    # Mapping dictionary for common misdetections
    item_mapping = {
        # Common misdetections
        'book': 'chocolate bar',  # Books often detected as chocolate bars
        'remote': 'chocolate bar',  # TV remotes can look like chocolate
        'cell phone': 'chocolate bar',  # Phones sometimes detected as chocolate
        'laptop': 'pizza box',  # Laptops might be pizza boxes
        'mouse': 'egg',  # Computer mouse vs eggs
        'keyboard': 'crackers',  # Keyboards vs cracker boxes

        # Keep food items as-is but make them more specific
        'bottle': 'bottle',
        'cup': 'cup',
        'bowl': 'bowl',
        'banana': 'banana',
        'apple': 'apple',
        'orange': 'orange',
        'carrot': 'carrot',
        'broccoli': 'broccoli',
        'pizza': 'pizza',
        'donut': 'donut',
        'cake': 'cake',
        'sandwich': 'sandwich',
        'hot dog': 'hot dog',

        # Generic items that could be food
        'person': 'mysterious leftovers',  # Sometimes people detected in fridge photos
        'chair': 'large container',
        'tv': 'microwave',
        'couch': 'large food container',
        'bed': 'pizza box',
        'dining table': 'cutting board',
        'toilet': 'mysterious container',  # Hopefully not actually in fridge!
        'car': 'very large container',
        'truck': 'industrial-sized container'
    }

    # Return mapped item or original if no mapping exists
    return item_mapping.get(detected_label.lower(), detected_label)

# Detection function
def detect_fridge_items(image_path):
    """Detect items in the fridge image using YOLO and map to fridge-appropriate items"""
    results = model(image_path)
    detected_items = []
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            # Map to more appropriate fridge item
            mapped_item = map_to_fridge_items(label)
            detected_items.append(mapped_item)

    # Remove duplicates while preserving order
    unique_items = []
    seen = set()
    for item in detected_items:
        if item.lower() not in seen:
            unique_items.append(item)
            seen.add(item.lower())

    return unique_items

# Random mood generator with lots of variety
def generate_mood(items):
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
            "Secretly judging your cereal choices"
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
            "Practicing advanced happiness therapy",
            "Plotting world domination through endorphins",
            "Being the MVP of your emotional stability",
            "Secretly training to be a mood enhancer"
        ],
        'fruit': [
            "Slowly accepting its inevitable browning fate",
            "Trying to stay fresh in a cold, dark world",
            "Dreaming of sunny orchards and better days",
            "Questioning why it ended up here",
            "Competing in a silent beauty contest",
            "Hoping to avoid the compost bin",
            "Living its best vitamin-packed life",
            "Photosynthesizing nostalgic memories"
        ],
        'vegetable': [
            "Wilting under the pressure of being healthy",
            "Secretly plotting a vitamin revolution",
            "Feeling green with envy of the chocolate",
            "Trying to convince you it tastes good",
            "Having a root awakening about life",
            "Leafing through its options",
            "Staying grounded despite the circumstances",
            "Branching out into new flavor territories"
        ],
        'condiment': [
            "Clinging to relevance one squeeze at a time",
            "Hoping to spice up your bland existence",
            "Waiting for its moment to shine",
            "Feeling salty about being forgotten",
            "Preserving itself for better times",
            "Adding flavor to an otherwise boring shelf life",
            "Bottling up its emotions",
            "Seasoning its words carefully"
        ],
        'generic': [
            "Just vibing in the cold darkness",
            "Living its best refrigerated life",
            "Chilling like a villain",
            "Keeping it cool under pressure",
            "Frozen in time and space",
            "Having a cool relationship with temperature",
            "Maintaining its composure in the cold",
            "Embracing the minimalist lifestyle"
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
        "Your fridge has developed commitment issues"
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
            "Meditating on the concept of nothingness"
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

        # Assign moods with some intelligence for specific items
        for item in items:
            item_lower = item.lower()

            # Give chocolate items chocolate-specific moods sometimes
            if any(word in item_lower for word in ['chocolate', 'bar', 'candy', 'sweet']):
                # 70% chance for chocolate-specific mood, 30% random
                if random.random() < 0.7:
                    mood = random.choice(mood_templates['chocolate'])
                else:
                    mood = random.choice(all_moods)
            # Give fruit items fruit-specific moods sometimes
            elif any(word in item_lower for word in ['apple', 'banana', 'orange', 'fruit', 'berry']):
                if random.random() < 0.6:
                    mood = random.choice(mood_templates['fruit'])
                else:
                    mood = random.choice(all_moods)
            # Everything else gets completely random mood
            else:
                mood = random.choice(all_moods)

            mood_lines.append(f"{item} – \"{mood}\"")

    # Add random final mood
    final_mood = random.choice(final_moods)
    mood_lines.append(f"Final Mood: {final_mood}")

    return "\n".join(mood_lines)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({"error": "No image part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filename = secure_filename(file.filename)
        unique_name = f"{uuid.uuid4().hex}{os.path.splitext(filename)[1]}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_name)
        file.save(file_path)

        # Detect fridge items
        items = detect_fridge_items(file_path)

        # Generate mood text
        mood = generate_mood(items)

        # --- STRUCTURED JSON RETURN WITH BACKWARD COMPATIBILITY ---
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
    return 'FridgeMood.AI Backend (No Duplicates) is running!'

if __name__ == '__main__':
    print("🚀 Starting FridgeMood.AI backend with duplicate removal...")
    app.run(debug=True, host='127.0.0.1', port=5000)
