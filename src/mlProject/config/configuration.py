from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directory
from mlProject.entity.config_entity import DataIngestionConfig



class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_APTH):

                 self.config = read_yaml(config_filepath)
                 self.params = read_yaml(params_filepath)
                 self.schema = read_yaml(schema_filepath)

                 create_directory([self.config.artifacts_root])   


    def get_data_ingestion_config(self) -> DataIngestionConfig:
                config = self.config.data_ingestion

                create_directory([config.root_dir])

                data_ingestion_config = DataIngestionConfig(
                        root_dir=config.root_dir,
                        source_URL= config.source_URL,
                        local_data_file= config.local_data_file
                )

                return data_ingestion_config
        