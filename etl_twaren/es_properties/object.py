import os
from dotenv import load_dotenv
load_dotenv()

data_es = {
    "end_point": os.getenv("DATA_ES_END_POINT"),
}

ml_es = {
    "end_point": os.getenv("ML_ES_END_POINT"),
}
