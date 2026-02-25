# from us_visa.pipline.training_pipeline import TrainPipeline



# obj = TrainPipeline()
# obj.run_pipeline()

from us_visa.logger import structlog

logging = structlog.get_logger(__name__)

logging.info("Entered the load_object method of utils")