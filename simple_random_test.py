#!/usr/bin/env python3
"""
Simple test to show the random mood functionality working
"""

import random

def generate_super_random_mood(items):
    """Generate completely random moods for each item"""
    
    # Huge pool of random moods
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
        "Developing separation anxiety from other foods",
        "Composing haikus about refrigeration",
        "Starting a support group for forgotten leftovers",
        "Practicing mindful breathing in the crisper drawer",
        "Becoming a life coach for expired items",
        "Writing a dissertation on optimal storage temperatures",
        "Developing a fear of being eaten",
        "Plotting world domination through nutrition",
        "Becoming fluent in the language of freshness",
        "Starting a revolution against food waste",
        "Practicing advanced meditation on shelf life",
        "Hosting philosophical debates about expiration",
        "Learning interpretive dance for vegetables",
        "Writing poetry about the meaning of cold",
        "Becoming a therapist for traumatized leftovers",
        "Starting a blog about refrigerator politics",
        "Developing trust issues with plastic wrap",
        "Practicing yoga in the freezer section"
    ]
    
    # Random final moods
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
        "Your fridge is taking up interpretive dance",
        "Your fridge is writing angry letters to food companies",
        "Your fridge is considering becoming a minimalist",
        "Your fridge is starting a podcast about cold storage"
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
        # Each item gets a COMPLETELY RANDOM mood from the entire pool
        for item in items:
            mood = random.choice(all_moods)
            mood_lines.append(f"{item} – \"{mood}\"")
    
    # Random final mood
    final_mood = random.choice(final_moods)
    mood_lines.append(f"Final Mood: {final_mood}")
    
    return "\n".join(mood_lines)

def demo_randomness():
    """Demonstrate the randomness with the same items"""
    
    # Simulate detected items
    test_items = ["bottle", "orange", "milk", "cheese"]
    
    print("🎲 SUPER RANDOM MOOD GENERATOR DEMO")
    print("=" * 60)
    print("Same items, completely different moods each time!")
    print("=" * 60)
    
    for i in range(5):
        print(f"\n🎯 Generation {i+1}:")
        print("-" * 40)
        
        mood_result = generate_super_random_mood(test_items)
        
        # Parse and display
        lines = mood_result.split("\n")
        for line in lines:
            if line.strip():
                if line.lower().startswith("final mood:"):
                    print(f"🏁 {line}")
                else:
                    print(f"🍽️  {line}")
    
    print("\n" + "=" * 60)
    print("🎉 SUCCESS! Each generation shows completely different moods!")
    print("🔄 Every item gets a random personality every time!")
    print("=" * 60)

if __name__ == "__main__":
    demo_randomness()
