How to set virtual env:

create new virtual env :

```
python -m venv venv
```

Run command:

```
pip install -r requirements.txt

```

Internal Use: Run this command to start the application

```
python3 app.py
```

Navigate to swagger url-

http://localhost:8080/docs

How to run create and run docker image of fastApi.

Run command to create docker image

```
docker build -t channel-sort-validator .
```

Run command to run docker image

```
docker run -p 8080:8080 channel-sort-validator
```

Navigate to swagger url-

http://localhost:8080/docs
