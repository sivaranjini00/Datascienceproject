from src.Datascienceproject import logger
from src.Datascienceproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.Datascienceproject.pipeline.data_validation_pipeline import DataValidationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Validation Stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        data_ingestion=DataValidationTrainingPipeline()
        data_ingestion.initiate_data_validation()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




