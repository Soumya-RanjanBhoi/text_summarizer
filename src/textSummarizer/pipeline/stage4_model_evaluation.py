from textSummarizer.config.configuration import ConfriguationManager
from textSummarizer.components.model_evaluation import ModelEvaluation
from textSummarizer.logging import logger


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config=ConfriguationManager()
            model_evaluation_config=config.get_model_evaluation_config()
            model_evaluation=ModelEvaluation(config=model_evaluation_config)
            model_evaluation.convert()
        except Exception as e:
            raise e