FROM python
RUN mkdir -p /app
WORKDIR /app
RUN cp -r . /app/
RUN pip install -r /app/requirements.txt
ENTRYPOINT ["python", "/app/src/app.py" ]
