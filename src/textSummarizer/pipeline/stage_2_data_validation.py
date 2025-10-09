from textSummarizer.config.configuration import ConfriguationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
           config=ConfriguationManager()
           data_validation_config=config.get_data_validation_config()
           data_validation=DataValidation(config=data_validation_config)
           data_validation.validate_all_files_exists()
        except Exception as e:
          raise e