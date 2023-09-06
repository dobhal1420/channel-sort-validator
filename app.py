import uvicorn
from fastapi import FastAPI
from fastapi import Form, UploadFile, File, HTTPException

from services.csvProcessor import CSVProcessor
from util.deviceType import DeviceType
from util.source import Source

app = FastAPI(title="Channel Sorting Validator", description="Helps in validating Channel sorting", version="0.0.1")


@app.get("/configuration")
async def get_configuration():
    return "Hello World!!"


@app.post("/validate")
async def validate(device_types: DeviceType = Form(..., description="Select a device type from the dropdown."),
                   source: Source = Form(..., description="Select a source from the dropdown."),
                   file1: UploadFile = File(...),
                   file2: UploadFile = File(...)):
    # Check if the uploaded file has a CSV extension
    if not file1.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Uploaded file1 must be in CSV format.")

    if not file2.filename.endswith('.json'):
        raise HTTPException(status_code=400, detail="Uploaded file2 must be in json format.")

    csv_data_processed = {}
    try:
        with CSVProcessor(file1) as csv_data:
            csv_data_processed = csv_data
    except HTTPException as e:
        raise e

    print(csv_data_processed)

    with open(file2.filename, "wb") as f2:
        f2.write(file2.file.read())

    return {"deviceTypes": device_types, "source": source}


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8080)
