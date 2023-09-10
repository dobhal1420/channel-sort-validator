import csv
import pandas as pd
from fastapi import UploadFile, HTTPException


class CSVProcessor:
    def __init__(self, file: UploadFile):
        self.file = file

    def __enter__(self):
        try:
            self.sorted_channel_data_tv_db_objects = []
            with self.file.file as csvfile:
                # Read TV DB File
                data = pd.read_csv(csvfile)
                # columns_to_print = ['display_number', 'display_name']
                # print(data[columns_to_print])

                # Filter based on channel type
                condition = data['type'] == 'TYPE_DVB_T2'
                filtered_data = data[condition]

                # Sort by LCN
                sorted_channel_data_tv_db_dataframe = filtered_data.sort_values(by="display_number", ascending=True)
                # print("After sorting")
                # print(sorted_data_tv_db[['display_number','display_name']])

                # Convert DataFrame to list of objects
                self.sorted_channel_data_tv_db_objects = sorted_channel_data_tv_db_dataframe.to_dict(orient='records')

            return self.sorted_channel_data_tv_db_objects
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing CSV: {str(e)}")

    def __exit__(self, exc_type, exc_value, traceback):
        pass
