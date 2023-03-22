from housing.entity.config_entit import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, \
    ModelPusherConfig, ModelEvaluationConfig, TrainingPipelineConfig

class Configuration:
    def __init__(slef):
        pass

    def get_ingestion_config() -> DataIngestionConfig:
        pass

    def get_data_validation_config() -> DataValidationConfig:
        pass

    def get_data_transformation_config() -> DataTransformationConfig:
        pass

    def get_model_trainer_config() -> ModelTrainerConfig:
        pass

    def ger_model_evlauation_config() -> ModelEvaluationConfig:
        pass

    def get_model_pusher_config() -> ModelPusherConfig:
        pass

    def get_training_pipeline_config() ->TrainingPipelineConfig:
        pass
