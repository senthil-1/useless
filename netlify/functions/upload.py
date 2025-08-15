import json
import random

def handler(event, context):
    """Netlify function for FridgeMood.AI upload"""
    
    # Handle CORS
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
    }
    
    # Handle preflight requests
    if event['httpMethod'] == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': ''
        }
    
    # Only allow POST requests
    if event['httpMethod'] != 'POST':
        return {
            'statusCode': 405,
            'headers': headers,
            'body': json.dumps({'error': 'Method not allowed'})
        }
    
    # Simulate item detection (since we can't run YOLO on Netlify)
    possible_items = [
        ["bottle", "orange", "milk"],
        ["chocolate bar", "apple", "cheese"],
        ["banana", "yogurt", "juice"],
        ["leftovers", "vegetables", "condiments"],
        ["pizza slice", "soda", "fruit"],
        ["bread", "butter", "eggs"],
        ["tomato", "lettuce", "onion"]
    ]
    
    items = random.choice(possible_items)
    
    # Generate random moods
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
        "Starting a podcast about cold storage"
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
    
    # Generate mood lines
    mood_lines = []
    moods_list = []
    
    for item in items:
        mood = random.choice(all_moods)
        mood_lines.append(f"{item} – \"{mood}\"")
        moods_list.append({
            "name": item,
            "mood": mood
        })
    
    final_mood = random.choice(final_moods)
    mood_lines.append(f"Final Mood: {final_mood}")
    
    mood_text = "\n".join(mood_lines)
    
    # Return response
    response_data = {
        "mood": mood_text,
        "moods": moods_list,
        "finalMood": final_mood,
        "filename": f"demo_{random.randint(1000, 9999)}.jpg"
    }
    
    return {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps(response_data)
    }
