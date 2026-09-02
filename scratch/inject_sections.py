import os

with open('missing_sections_utf8.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()
    
# Take only the first 158 lines (everything before the DEPOIMENTOS start)
inject_content = "".join(lines[:158])

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

target = """    <!-- ==========================================
         DEPOIMENTOS
         ========================================== -->"""

if target in content:
    new_content = content.replace(target, inject_content + "\n" + target)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Injected successfully!")
else:
    print("Target not found in index.html")
