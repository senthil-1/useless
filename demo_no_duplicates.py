#!/usr/bin/env python3
"""
Demonstrate the duplicate removal fix working
"""

import random

def remove_duplicates(items):
    """Remove duplicates while preserving order"""
    unique_items = []
    seen = set()
    for item in items:
        if item.lower() not in seen:
            unique_items.append(item)
            seen.add(item.lower())
    return unique_items

def generate_random_mood(items):
    """Generate random moods for unique items only"""
    
    # Remove duplicates first
    unique_items = remove_duplicates(items)
    
    # Random moods pool
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
        "Keeping it cool under pressure"
    ]
    
    final_moods = [
        "Your fridge is having a midlife crisis",
        "Your fridge is in therapy and making progress", 
        "Your fridge has trust issues with expiration dates",
        "Your fridge is living its best chaotic life",
        "Your fridge needs a vacation from your eating habits"
    ]
    
    mood_lines = []
    
    if not unique_items:
        mood_lines.append("Fridge – \"Empty. Existential dread detected\"")
    else:
        # Each UNIQUE item gets a random mood
        for item in unique_items:
            mood = random.choice(all_moods)
            mood_lines.append(f"{item} – \"{mood}\"")
    
    # Random final mood
    final_mood = random.choice(final_moods)
    mood_lines.append(f"Final Mood: {final_mood}")
    
    return "\n".join(mood_lines)

def demo_duplicate_removal():
    """Demonstrate the fix working"""
    
    print("🎯 DUPLICATE REMOVAL DEMONSTRATION")
    print("=" * 60)
    
    # Simulate YOLO detection with duplicates (like "2 bottles")
    simulated_detections = [
        "bottle", "bottle", "orange", "refrigerator"  # 2 bottles detected
    ]
    
    print("📸 Simulated YOLO Detection Results:")
    print(f"Raw detections: {simulated_detections}")
    print(f"Count: {len(simulated_detections)} items detected")
    
    print("\n🔧 BEFORE Fix (with duplicates):")
    print("Items that would get moods:")
    for i, item in enumerate(simulated_detections, 1):
        print(f"  {i}. {item}")
    print("❌ Problem: 'bottle' appears twice!")
    
    print("\n✅ AFTER Fix (duplicates removed):")
    unique_items = remove_duplicates(simulated_detections)
    print(f"Unique items: {unique_items}")
    print(f"Count: {len(unique_items)} unique items")
    print("Items that get moods:")
    for i, item in enumerate(unique_items, 1):
        print(f"  {i}. {item}")
    print("✅ Success: Each item appears only once!")
    
    print("\n🎭 Generated Moods (No Duplicates):")
    print("-" * 40)
    mood_result = generate_random_mood(simulated_detections)
    for line in mood_result.split("\n"):
        if line.strip():
            print(f"  {line}")
    
    print("\n" + "=" * 60)
    print("🎉 FIXED! No more duplicate items in mood analysis!")
    print("Each unique item gets exactly one mood entry.")

if __name__ == "__main__":
    demo_duplicate_removal()
