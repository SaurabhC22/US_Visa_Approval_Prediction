import os
from pathlib import Path

project_name = "US-Visa"   ## Root Folder

list_of_files = [
    
    f"{project_name}/__init__.py"   ## "__init__.py as constructor file in project_name
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    
    f"{project_name}/config/__init__.py",            ## For now only cretaed constructor file 
    
    f"{project_name}/constants/__init__.py",
    
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/config/artifact_entity.py",
    
    f"{project_name}/exception/__init__.py",
    
    f"{project_name}/logger/__init__.py",
    
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
     "config/model.yaml",
    "config/schema.yaml",
]

for filepath in list_of_files:
    filepath = Path(filepath)  ## This path is used to check the Operating system 
    filedir, filename = os.path.split(filepath)   ## It split folders in filedir and filenames in filename sperately
    if filedir != "":                        ## Creates Directory
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):    ## Creates file  and alo check if the file exists ad have data then it does not create it again, but if the file is empty then the file is re created   
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")