import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract professionals-gallery-section
gallery_pattern = re.compile(r'(<section class="section professionals-gallery-section" id="categorias">.*?</section>\n)', re.DOTALL)
match = gallery_pattern.search(content)
if match:
    gallery_html = match.group(1)
    
    # Remove it from its current position
    content = content.replace(gallery_html, '')
    
    # Insert it right before <!-- ========================================== BUSCA
    insert_pattern = r'(\s*<!-- ==========================================\s*BUSCA)'
    content = re.sub(insert_pattern, '\n\n    ' + gallery_html.strip() + '\\1', content, count=1)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Section moved successfully")
else:
    print("Could not find gallery section")
