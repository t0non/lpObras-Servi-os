import subprocess

def get_git_file(commit, filename):
    result = subprocess.run(['git', 'show', f'{commit}:{filename}'], capture_output=True, check=True)
    return result.stdout.decode('utf-8')

old_content = get_git_file('e451d26', 'index.html')
lines = old_content.splitlines(keepends=True)

start_index = -1
end_index = -1

for i, line in enumerate(lines):
    if "SOBRE OS / BANNER CTA (Substituindo 'Por que usar a OS?')" in line:
        start_index = i - 1 # Include the previous line (which is the start of the comment block)
    if "DEPOIMENTOS" in line and start_index != -1 and end_index == -1:
        end_index = i - 1
        break

if start_index != -1 and end_index != -1:
    inject_content = "".join(lines[start_index:end_index])
    
    with open('index.html', 'r', encoding='utf-8') as f:
        current_content = f.read()
        
    target = """    <!-- ==========================================
         DEPOIMENTOS
         ========================================== -->"""
         
    if target in current_content:
        new_content = current_content.replace(target, inject_content + "\n" + target)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Injected successfully!")
    else:
        print("Target not found in current index.html")
else:
    print(f"Indices not found: start={start_index}, end={end_index}")
