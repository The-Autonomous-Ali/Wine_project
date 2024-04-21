from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject.logging import logger


STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config= ConfigurationManager()
    data_Ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_Ingestion_config)
    data_ingestion.download_file()
    


if __name__ =='__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<\n\nx======")

    except Exception as e:
        logger.exception(e)
        raise e