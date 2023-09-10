import uvicorn
from fastapi import FastAPI
from fastapi import Form, UploadFile, File, HTTPException

from services.csvProcessor import CSVProcessor
from services.jsonProcessor import JSONProcessor
from services.sortorderValidator import SortOrderValidator
from util.deviceType import DeviceType
from util.source import Source

app = FastAPI(title="Channel Sorting Validator", description="Helps in validating Channel sorting", version="0.0.1")


@app.get("/configuration")
async def get_configuration():
    return "Hello World!!"


@app.post("/validate")
async def validate(device_types: DeviceType = Form(..., description="Select a device type from the dropdown."),
                   channel_source: Source = Form(..., description="Select a source from the dropdown."),
                   tv_db_file: UploadFile = File(...),
                   pre_sort_file: UploadFile = File(...)):
    # Check if the uploaded file has a CSV extension
    if not tv_db_file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Uploaded tv_db_file must be in CSV format.")

    if not pre_sort_file.filename.endswith('.json'):
        raise HTTPException(status_code=400, detail="Uploaded pre_sort_file must be in json format.")

    validator = SortOrderValidator(tv_db_file, pre_sort_file)
    validator.validate()

    return {"deviceTypes": device_types, "source": channel_source}


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8080)
