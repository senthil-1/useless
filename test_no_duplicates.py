#!/usr/bin/env python3
"""
Test duplicate removal functionality
"""

def remove_duplicates(items):
    """Remove duplicates while preserving order"""
    unique_items = []
    seen = set()
    for item in items:
        if item.lower() not in seen:
            unique_items.append(item)
            seen.add(item.lower())
    return unique_items

def test_duplicate_removal():
    """Test the duplicate removal logic"""
    
    print("🧪 Testing Duplicate Removal Logic")
    print("=" * 50)
    
    # Test cases
    test_cases = [
        {
            "name": "Multiple bottles",
            "input": ["bottle", "bottle", "orange", "bottle"],
            "expected": ["bottle", "orange"]
        },
        {
            "name": "Mixed case duplicates", 
            "input": ["Bottle", "bottle", "BOTTLE", "Orange"],
            "expected": ["Bottle", "Orange"]
        },
        {
            "name": "Chocolate bars from books",
            "input": ["chocolate bar", "bottle", "chocolate bar", "orange", "chocolate bar"],
            "expected": ["chocolate bar", "bottle", "orange"]
        },
        {
            "name": "No duplicates",
            "input": ["bottle", "orange", "milk"],
            "expected": ["bottle", "orange", "milk"]
        },
        {
            "name": "All same items",
            "input": ["bottle", "bottle", "bottle", "bottle"],
            "expected": ["bottle"]
        }
    ]
    
    for test_case in test_cases:
        print(f"\n📋 Test: {test_case['name']}")
        print(f"Input:    {test_case['input']}")
        
        result = remove_duplicates(test_case['input'])
        print(f"Output:   {result}")
        print(f"Expected: {test_case['expected']}")
        
        if result == test_case['expected']:
            print("✅ PASS")
        else:
            print("❌ FAIL")
    
    print("\n" + "=" * 50)
    print("🎯 This logic should be applied to detected items!")

if __name__ == "__main__":
    test_duplicate_removal()
