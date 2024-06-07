import os
from pathlib import Path

 ## Automatically take care of system path (wondows, linux)

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/util.py",
    "src/logger/logging.py",
    "src/exception/exception",
    "tests/__init__.py",
    "tests/unit/__init__.py",
     "tests/intergration/__init__.py",
     "init_setup.sh",
     "requirements.txt",
     "requirements_dev.txt",
    "setup.py",
    "setup.config",
    "pyproject.toml",
    "tox.ini",
    "expirement/experiments.ipynb",



]

for filepath in list_of_files:
    file_name = Path(filepath)
    filedir,file = os.path.split(file_name)
    if filedir!="":
        os.makedirs(filedir,exist_ok = True)
    if (not os.path.exists(file_name)) or (os.path.getsize(file_name) == 0):
        with open(file_name, "w") as f:
            pass 