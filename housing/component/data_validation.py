
from housing .exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact
import os,sys



class DataValidation:

    def __init__(self, data_validation_config:DataValidationConfig, data_ingestion_artifact:DataIngestionArtifact):
        try:
            logging.info(f"{'='*20}Data validation log started{'='*20}")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e
        

    def initiate_data_validation(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e