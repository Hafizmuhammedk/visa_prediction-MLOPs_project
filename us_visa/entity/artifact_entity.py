from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str
