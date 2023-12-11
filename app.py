import uvicorn
from fastapi import FastAPI
from fastapi import Form, UploadFile, File, HTTPException

from services.csvProcessor import CSVProcessor
from services.jsonProcessor import JSONProcessor
from services.sortorderValidator import SortOrderValidator
from util.deviceType import DeviceType
from util.source import Source
from util.country import Country

app = FastAPI(title="Channel Sorting Validator", description="Helps in validating Channel sorting", version="0.0.1")


@app.get("/healthcheck")
async def get_endpoint_health_check():
    return "Endpoint health check is Green"


@app.post("/validate")
async def validate(device_types: DeviceType = Form(..., description="Select a device type from the dropdown."),
                   channel_source: Source = Form(..., description="Select a source from the dropdown."),
                   country: Country = Form(..., description="Select a country from the dropdown."),
                   tv_db_file: UploadFile = File(...),
                   pre_sort_file: UploadFile = File(..., description="Pull pre-sort file from TV using this command via adb. Example: adb pull /tvconfig/config/name_sorting/DVBS_DEU.json ")):
    # Check if the uploaded file has a CSV extension
    if not tv_db_file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Uploaded tv_db_file must be in CSV format.")

    # Check if the uploaded file has a json extension
    if not pre_sort_file.filename.endswith('.json'):
        raise HTTPException(status_code=400, detail="Uploaded pre_sort_file must be in json format.")

    validator = SortOrderValidator(channel_source, tv_db_file, pre_sort_file)
    return validator.validate()


    #return {"deviceTypes": device_types, "source": channel_source, "country": country}


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8080)
