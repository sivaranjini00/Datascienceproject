import os
import yaml
from src.Datascienceproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

from pathlib import Path
from box import ConfigBox
import yaml
from ensure import ensure_annotations
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories

    Args:
        path_to_directories (list): list of path of directories
        verbose (bool, optional): _description_. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save dict as json file

    Args:
        path (Path): path to json file
        data (dict): data to be saved
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    load json file and returns as ConfigBox

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: ConfigBox type
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded from: {path}")
    return ConfigBox(content)
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    save any data type as binary file

    Args:
        data (Any): data to be saved
        path (Path): path to binary file
    """
    joblib.dump(data, path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    load binary file and returns data

    Args:
        path (Path): path to binary file

    Returns:
        Any: data stored in binary file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data






    

