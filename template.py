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
    f"src/{project_name}/logging/__init__.py", # Init file for logging
    f"src/{project_name}/config/__init__.py", # Init file for configuration
    f"src/{project_name}/config/configuration.py", # Configuration settings
    f"src/{project_name}/pipeline/__init__.py", # Init file for pipeline
    f"src/{project_name}/entity/__init__.py", # Init file for entities
    f"src/{project_name}/constants/__init__.py", # Init file for constants
    "config/config.yaml", # Configuration file
    "params.yaml", # Parameters file
    "app.py", # Main application file
    "main.py", # Main execution file
    "Dockerfile", # Docker configuration file
    "requirements.txt", # Requirements file
    "setup.py", # Setup file for packaging
    "research/trials.ipynb", # Jupyter notebook for research and trials
]

# Create necessary directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            logging.info(f"Creating empty file: {filepath}")
            pass
    else:
        logging.info(f"File already exists: {filepath}, skipping creation.")
        

