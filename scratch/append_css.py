import subprocess
import os

# Get the old CSS
result = subprocess.run(['git', 'show', 'ce8a27e:css/about-os.css'], capture_output=True, check=True)
old_css = result.stdout.decode('utf-8')

# Append to current CSS
with open('css/about-os.css', 'a', encoding='utf-8') as f:
    f.write("\n\n" + old_css)
    
print("Appended successfully!")
