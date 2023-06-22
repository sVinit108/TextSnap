import os
import logging
from pathlib import Path

'''template.py creates the required folder structure automatically'''

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "TextSnap"

file_list = [
    # github file
    ".github/workflow/.gitkeep", 
    # src folder
    f"src/{project_name}/__init__.py",
    # src/components folder
    f"src/{project_name}/components/__init__.py",
    # src/utils folder
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    # src/logging folder
    f"src/{project_name}/logging/__init__.py",
    # src/config folder
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    # src/pipeline folder
    f"src/{project_name}/pipeline/__init__.py",
    # src/entity folder
    f"src/{project_name}/entity/__init__.py",
    # src/constant folder
    f"src/{project_name}/constant/__init__.py",
    # config yaml file
    "config/config.yaml",
    # params yaml file
    "params.yaml",
    # app file
    "app.py",
    # main file
    "main.py",
    # Docker image file
    "Dockerfile",
    # requirements file 
    "requirements.txt",
    # setup file
    "setup.py",
    # research folder
    "research/trials.ipynb",
]

for file in file_list:
    filepath=Path(file)
    filedir,filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created directory {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating empty file {filename}")

    else:
        logging.info(f"{filename} already exists")