import sys

from pandas import DataFrame
from sklearn.pipeline import Pipeline

from us_visa.exception import USvisaException
from dotenv import load_dotenv
from us_visa.logger import structlog

logging = structlog.get_logger(__name__)

load_dotenv()


class TargetValueMapping:
    def __init__(self):
        self.Certified:int = 0
        self.Denied:int = 1
    def _asdict(self):
        return self.__dict__
    def reverse_mapping(self):
        mapping_response = self._asdict()