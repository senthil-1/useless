#!/usr/bin/env python3
"""
Test the mood randomness directly without the server
"""

import random

def generate_random_mood(items):
    """Generate random, humorous moods for fridge items"""
    
    # Create a pool of ALL possible moods for maximum randomness
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
        # Assign completely random moods to each item
        for item in items:
            # Each item gets a completely random mood from the entire pool
            mood = random.choice(all_moods)
            mood_lines.append(f"{item} – \"{mood}\"")
    
    # Add random final mood
    final_mood = random.choice(final_moods)
    mood_lines.append(f"Final Mood: {final_mood}")
    
    return "\n".join(mood_lines)

def test_randomness():
    """Test that the mood generator produces different results"""
    
    # Test items (simulating detected items)
    test_items = ["bottle", "orange", "milk", "cheese"]
    
    print("🧪 Testing Mood Randomness")
    print("=" * 50)
    
    # Generate 5 different mood sets
    for i in range(5):
        print(f"\n🎲 Test {i+1}:")
        mood_result = generate_random_mood(test_items)
        
        # Parse and display results
        lines = mood_result.split("\n")
        for line in lines:
            if line.strip():
                if line.lower().startswith("final mood:"):
                    print(f"📝 {line}")
                else:
                    print(f"🍽️ {line}")
    
    print("\n" + "=" * 50)
    print("✅ Each test should show different moods for the same items!")

if __name__ == "__main__":
    test_randomness()
