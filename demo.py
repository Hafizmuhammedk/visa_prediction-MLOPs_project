# from dotenv import load_dotenv
# load_dotenv()

from us_visa.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()