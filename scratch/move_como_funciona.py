import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for the "Como funciona?" section
pattern = re.compile(r'( {4}<!-- ==========================================\n         COMO FUNCIONA\n         ========================================== -->\n    <section class="section section--white" id="como-funciona">.*?</section>\n)', re.DOTALL)
match = pattern.search(content)

if match:
    section_html = match.group(1)
    # Remove from current location
    content = content.replace(section_html, '')
    
    # Target location: right before "BUSCA (Nova Aba Premium)"
    target_pattern = r'( {4}<!-- ==========================================\n         BUSCA \(Nova Aba Premium\))'
    content = re.sub(target_pattern, section_html + '\n\\1', content, count=1)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Move successful")
else:
    print("Could not find the section")
