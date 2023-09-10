from http.client import HTTPException
from fastapi import UploadFile, HTTPException
from services.csvProcessor import CSVProcessor
from services.jsonProcessor import JSONProcessor
import json


class SortOrderValidator:
    def __init__(self, tv_db_file: UploadFile, presort_file: UploadFile):
        self.tv_db_file = tv_db_file
        self.presort_file = presort_file

    def validate(self):
        sorted_channel_data_tv_db_objects = {}
        try:
            with CSVProcessor(self.tv_db_file) as csv_data:
                sorted_channel_data_tv_db_objects = csv_data
        except HTTPException as e:
            raise e

        json_pre_sort_channel_dict = {}
        try:
            with JSONProcessor(self.presort_file) as presort_data:
                json_pre_sort_channel_dict = presort_data
        except HTTPException as e:
            raise e

        print(json_pre_sort_channel_dict)

        # Verify TV DB data is in accordance with pre-sort JSON file
        json_prev_channel_rank = 0
        overflow_channel_data_list = []

        for channel_tv_db in sorted_channel_data_tv_db_objects:

            channel_name_tv_db = str(channel_tv_db['display_name'])
            channel_number_tv_db = int(channel_tv_db['display_number'])

            json_current_pointer_rank = json_pre_sort_channel_dict.get(channel_name_tv_db)
            if json_current_pointer_rank is not None:
                if json_current_pointer_rank > json_prev_channel_rank:
                    json_prev_channel_rank = json_current_pointer_rank

                else:
                    print("Channel Order Mismatch - " + channel_name_tv_db + " is placed at LCN " + str(
                        channel_number_tv_db))

            else:
                print("Overflow Area - Channel " + channel_name_tv_db + " at LCN " + str(
                    channel_number_tv_db) + " does not exist in presort json file")
                # list of channel TV DB
                overflow_channel_data_list.append(channel_tv_db)

        # Overflow Area processing

        for overflow_channel_data in overflow_channel_data_list:
            overflow_channel_name = str(overflow_channel_data['display_name'])
            overflow_channel_rank = int(overflow_channel_data['display_number'])
            overflow_channel_type = overflow_channel_data['service_type']
            overflow_channel_format = overflow_channel_data['video_format']
            overflow_channel_subscription_str = overflow_channel_data['internal_provider_data']
            overflow_channel_subscription_object = json.loads(overflow_channel_subscription_str)

            print("Channel Data - " + overflow_channel_name + " , " + str(
                overflow_channel_rank) + " , " + overflow_channel_type + " , " + overflow_channel_format
                  + " , " + str(overflow_channel_subscription_object['scrambled']))





