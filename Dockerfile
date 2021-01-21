FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install mysqlclient python-dotenv
RUN pip install -r requirements.txt
COPY . /code/
RUN ["chmod", "+x", "./scripts/entrypoint.sh"]
ENTRYPOINT ["sh","./scripts/entrypoint.sh"]
