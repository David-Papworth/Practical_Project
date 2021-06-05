FROM python:latest
WORKDIR /app
RUN pip install flask requests flask_sqlalchemy pymysql
COPY . .
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]