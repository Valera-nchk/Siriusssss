import webbrowser
import os

html_file = os.path.join(os.path.dirname(__file__), "кодик.html")

webbrowser.open(f"file://{html_file}")
