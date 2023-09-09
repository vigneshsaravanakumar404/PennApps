from taipy import Gui
from taipy.gui import Html

html = Html("""
    
""")

Gui(page=html, css_file='./styles.css').run(dark_mode=False)
