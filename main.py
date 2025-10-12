from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_2_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage3_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage4_model_evaluation import ModelEvaluationTrainingPipeline

# STAGE_NAME="Data Ingestion stage"
# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     data_ingestion=DataIngestionTrainingPipeline()
#     data_ingestion.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n x=====x")

# except Exception as e:
#     logger.exception(e)
#     raise e

# STAGE_NAME="Data validation stage"
# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     data_validation=DataValidationTrainingPipeline()
#     data_validation.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n x=====x")

# except Exception as e:
#     logger.exception(e)
#     raise e


# STAGE_NAME="Data transformation stage"
# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     data_transformation=DataTransformationTrainingPipeline()
#     data_transformation.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n x=====x")

# except Exception as e:
#     logger.exception(e)
#     raise e


STAGE_NAME="model evaluation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_evaluation=ModelEvaluationTrainingPipeline()
    data_evaluation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n x=====x")

except Exception as e:
    logger.exception(e)
    raise e