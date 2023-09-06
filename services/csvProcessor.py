import csv

from fastapi import UploadFile, HTTPException


class CSVProcessor:
    def __init__(self, file: UploadFile):
        self.file = file

    def __enter__(self):
        try:
            self.data = []
            with self.file.file as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.data.append(row)
            return self.data
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing CSV: {str(e)}")

    def __exit__(self, exc_type, exc_value, traceback):
        pass
