FROM python:3.6-stretch
ENV FLASK_ENV=development

COPY . ./api
WORKDIR ./api
RUN pip install -r requirements.txt

EXPOSE 8181

ENTRYPOINT ["python", "main.py"]
