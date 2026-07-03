import os
import sys
import re

def check_files_exist():
    required_files = [
        'details.txt', 'q1.py', 'q4.py', 'q5.py', 'q7.py', 'q8.py', 'q9.py', 'q10.py', 'q12.py',
        'q11_1.py', 'q11_2.py'
    ]
    # Add q2_*.py and q3_*.py and q6_*.py
    for i in range(1, 11):
        required_files.append(f'q2_{i}.py')
    for i in range(1, 11):
        required_files.append(f'q3_{i}.py')
    for i in range(1, 6):
        required_files.append(f'q6_{i}.py')

    missing_files = []
    for file in required_files:
        if not os.path.exists(os.path.join('submission', file)):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        return False
    else:
        print("✅ All required files present.")
        return True

def check_comments():
    files_to_check = [f for f in os.listdir('submission') if f.endswith('.py')]
    files_without_comments = []
    
    for file in files_to_check:
        with open(os.path.join('submission', file), 'r') as f:
            content = f.read()
            # Look for comments that are not the boilerplate commit comment
            lines = content.split('\n')
            has_custom_comment = False
            for line in lines:
                stripped = line.strip()
                if stripped.startswith('#') and 'Commit the transaction' not in stripped:
                    has_custom_comment = True
                    break
            
            if not has_custom_comment:
                files_without_comments.append(file)
    
    if files_without_comments:
        print(f"❌ Files missing documentation: {', '.join(files_without_comments)}")
        return False
    else:
        print("✅ All Python files have documentation.")
        return True

def check_details_txt():
    if not os.path.exists('submission/details.txt'):
        print("❌ details.txt missing")
        return False
    
    with open('submission/details.txt', 'r') as f:
        content = f.read().strip()
        if not content:
            print("❌ details.txt is empty")
            return False
        # Basic check for ID format (assuming 9 digits)
        if not re.search(r'\d{9}', content):
            print("⚠️ details.txt might be missing a valid ID (9 digits)")
            # Not failing, just warning
    
    print("✅ details.txt present and not empty.")
    return True

if __name__ == "__main__":
    print("--- Starting Submission Checks ---")
    files_ok = check_files_exist()
    comments_ok = check_comments()
    details_ok = check_details_txt()
    
    if files_ok and comments_ok and details_ok:
        print("\n🎉 PASSED: Submission looks good!")
    else:
        print("\n⚠️ FAILED: Please fix the issues above.")
