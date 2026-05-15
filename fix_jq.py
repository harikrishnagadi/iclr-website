import re

with open('index.html', 'r') as f:
    html = f.read()

# Restore jQuery script
jquery_script = '<script defer src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>\n  <script defer src="static/js/fontawesome.all.min.js"></script>'
html = html.replace('<script defer src="static/js/fontawesome.all.min.js"></script>', jquery_script)

# Add id="video-showcase" and id="BibTeX" to their respective tags properly
html = html.replace('<section class="hl-section reveal">\n      <div class="u-center"', '<section id="video-showcase" class="hl-section reveal">\n      <div class="u-center"')

with open('index.html', 'w') as f:
    f.write(html)

with open('static/js/index.js', 'r') as f:
    js = f.read()

js = js.replace('document.addEventListener("DOMContentLoaded", function () {', '$(document).ready(function () {')

with open('static/js/index.js', 'w') as f:
    f.write(js)

print("Restored jQuery and fixed IDs")
