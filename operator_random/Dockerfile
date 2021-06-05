FROM python:latest
WORKDIR /app
RUN pip install flask 
COPY . .
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]