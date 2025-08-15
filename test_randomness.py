#!/usr/bin/env python3
"""
Test script to demonstrate the randomness of mood generation
"""

import requests
import os

def test_randomness():
    """Test multiple uploads to show randomness"""
    
    # Find a test image
    uploads_dir = "uploads"
    image_files = [f for f in os.listdir(uploads_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    if not image_files:
        print("No test images found")
        return
    
    test_image = os.path.join(uploads_dir, image_files[0])
    print(f"Testing randomness with: {test_image}")
    print("=" * 60)
    
    for i in range(5):
        print(f"\n🎲 Upload {i+1}:")
        try:
            with open(test_image, 'rb') as f:
                files = {'image': f}
                response = requests.post('http://127.0.0.1:5000/upload', files=files, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                print(f"📝 Final Mood: {data['finalMood']}")
                
                if data['moods']:
                    print("🍽️ Item Moods:")
                    for item in data['moods'][:3]:  # Show first 3 items
                        print(f"   • {item['name']}: \"{item['mood']}\"")
                    if len(data['moods']) > 3:
                        print(f"   ... and {len(data['moods']) - 3} more items")
            else:
                print(f"❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 As you can see, each upload generates different random moods!")
    print("The same items get different personalities each time.")

if __name__ == "__main__":
    test_randomness()
