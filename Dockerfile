FROM python
RUN mkdir -p /app
WORKDIR /app
RUN cp . /app/
RUN pip install -r /app/requirements.txt
ENTRYPOINT ["python", "/app/src/app.py" ]
