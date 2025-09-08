import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO,format='[%(asctime)s] %(levelname)s - %(message)s')
project_name = "text_summarizer"

list_of_files = [
    ".github/workflows/.gitkeep", # Directory for GitHub configurations for CI/CD
    f"src/{project_name}/__init__.py", # Init file for the main package
    f"src/{project_name}/components/__init__.py", # Init file for components
    f"src/{project_name}/utils/__init__.py", # Init file for utilities
    f"src/{project_name}/utils/common.py", # Init file for utilities
    
]