#!/usr/bin/env python3
"""
Simple server test
"""

import requests
import os
import time

def test_server():
    """Test if server is responding"""
    
    print("🧪 Testing Server Response")
    print("=" * 40)
    
    # Test root endpoint
    try:
        response = requests.get('http://127.0.0.1:5000/', timeout=5)
        print(f"✅ Server responding: {response.text}")
    except Exception as e:
        print(f"❌ Server not responding: {e}")
        return False
    
    # Test upload endpoint
    uploads_dir = "uploads"
    if not os.path.exists(uploads_dir):
        print("❌ No uploads directory")
        return False
    
    image_files = [f for f in os.listdir(uploads_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    if not image_files:
        print("❌ No test images")
        return False
    
    test_image = os.path.join(uploads_dir, image_files[0])
    print(f"📸 Testing upload with: {test_image}")
    
    try:
        with open(test_image, 'rb') as f:
            files = {'image': f}
            response = requests.post('http://127.0.0.1:5000/upload', files=files, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Upload successful!")
            print(f"📊 Number of items detected: {len(data.get('moods', []))}")
            
            if data.get('moods'):
                print("🎭 Detected items and moods:")
                for item in data['moods']:
                    print(f"   • {item['name']}: \"{item['mood']}\"")
                print(f"🏁 Final mood: {data.get('finalMood', 'N/A')}")
                return True
            else:
                print("❌ No items detected in response")
                return False
        else:
            print(f"❌ Upload failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Upload error: {e}")
        return False

if __name__ == "__main__":
    # Wait a moment for server to start
    print("⏳ Waiting for server to start...")
    time.sleep(2)
    
    success = test_server()
    
    if success:
        print("\n🎉 Server is working correctly!")
    else:
        print("\n❌ Server has issues!")
