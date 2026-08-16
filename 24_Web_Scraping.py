# Day 24 - Basic HTML scraping using simple string parsing

sample_html = """
<html>
    <body>
        <h1 class="title">Welcome to Python Scraping</h1>
        <p class="description">This is a paragraph of text on a web page.</p>
    </body>
</html>
"""

# Extracting content between tags simply as a beginner
def extract_tag_content(html, tag):
    start_tag = "<" + tag + ">" if "<" + tag + ">" in html else 'class="'
    start_pos = html.find(">") + 1
    end_pos = html.find("</" + tag + ">")
    return html[start_pos:end_pos].strip()

print("Extracted HTML Data:")
print("Heading:", extract_tag_content(sample_html, "h1"))