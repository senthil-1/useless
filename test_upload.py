#!/usr/bin/env python3
"""
Test script to verify the upload functionality works correctly
"""

import requests
import os
import sys

def test_upload_endpoint():
    """Test the upload endpoint with a sample image"""
    
    # Check if server is running
    try:
        response = requests.get('http://127.0.0.1:5000/', timeout=5)
        print("✓ Server is accessible")
    except requests.exceptions.RequestException as e:
        print(f"✗ Server is not accessible: {e}")
        print("Please start the Flask server first with: python app_structured.py")
        return False
    
    # Find a test image in uploads folder
    uploads_dir = "uploads"
    if not os.path.exists(uploads_dir):
        print(f"✗ Uploads directory '{uploads_dir}' not found")
        return False
    
    # Get the first image file
    image_files = [f for f in os.listdir(uploads_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    if not image_files:
        print(f"✗ No image files found in '{uploads_dir}' directory")
        return False
    
    test_image = os.path.join(uploads_dir, image_files[0])
    print(f"Using test image: {test_image}")
    
    # Test the upload endpoint
    try:
        with open(test_image, 'rb') as f:
            files = {'image': f}
            response = requests.post('http://127.0.0.1:5000/upload', files=files, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            print("✓ Upload successful!")
            print(f"Response keys: {list(data.keys())}")
            
            # Check for expected response format
            if 'mood' in data:
                print("✓ Legacy 'mood' field present")
            if 'moods' in data:
                print(f"✓ Structured 'moods' field present with {len(data['moods'])} items")
            if 'finalMood' in data:
                print(f"✓ 'finalMood' field present: {data['finalMood']}")
            if 'filename' in data:
                print(f"✓ 'filename' field present: {data['filename']}")
            
            return True
        else:
            print(f"✗ Upload failed with status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"✗ Upload request failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing upload functionality...")
    print("=" * 50)
    
    success = test_upload_endpoint()
    
    print("=" * 50)
    if success:
        print("✓ All tests passed! Upload functionality is working correctly.")
        sys.exit(0)
    else:
        print("✗ Tests failed. Please check the issues above.")
        sys.exit(1)
