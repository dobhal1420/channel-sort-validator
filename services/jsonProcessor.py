from fastapi import UploadFile, HTTPException
from pandas._libs import json
import pandas as pd
import json


class JSONProcessor:
    def __init__(self, file: UploadFile):
        self.file = file

    def __enter__(self):
        try:
            self.json_pre_sort_channel_dict = {}
            with self.file.file as jsonfile:

                json_presort_data_list = json.load(jsonfile)

                # Extract Name and Rank from json to dict.
                for json_presort_data in json_presort_data_list:
                    channel_name = json_presort_data['name']
                    channel_rank = json_presort_data['rank']
                    if channel_name in self.json_pre_sort_channel_dict.keys():
                        print(
                            "Duplicate channel name in json. Please upload the correct json with unique channels - " + channel_name)
                    else:
                        self.json_pre_sort_channel_dict[channel_name] = channel_rank

            return self.json_pre_sort_channel_dict
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing Pre-sort File: {str(e)}")

    def __exit__(self, exc_type, exc_value, traceback):
        pass
