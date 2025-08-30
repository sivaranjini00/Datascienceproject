from src.Datascienceproject import logger
from src.Datascienceproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.Datascienceproject.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.Datascienceproject.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline     
from src.Datascienceproject.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
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

STAGE_NAME = "Data Transformation Stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        data_ingestion = DataTransformationTrainingPipeline()
        data_ingestion.initiate_data_transformation()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Trainer Stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        data_ingestion = ModelTrainerTrainingPipeline()
        data_ingestion.initiate_model_training()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e









