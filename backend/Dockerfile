FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./entrypoint.sh /code/entrypoint.sh
COPY ./todo .
RUN chmod +x /code/entrypoint.sh
#ENTRYPOINT ["/code/entrypoint.sh"]

