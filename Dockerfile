# Use the official Python image as the base image
FROM python:3.9

# Copy the files from the local directory to the image
COPY ./app.py /app/app.py
COPY ./services /app/services
COPY ./util /app/util
COPY ./requirements.txt /app/requirements.txt

# Run the commands inside the image
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
WORKDIR /app
EXPOSE 8080
CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8080"]

