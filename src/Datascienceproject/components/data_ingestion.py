import os
import urllib.request as request
from src.Datascienceproject import logger
import zipfile
from src.Datascienceproject.entity.config_entity import (DataIngestionConfig)



## component: data ingestion
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with File folowing info: {headers}")
        else:
            logger.info(f"File already exists of path")
    

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file to the data directory
        fuction returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
