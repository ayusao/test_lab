# Use an official Python runtime as a parent image
FROM python:3.9

WORKDIR /app
COPY . /app
RUN pip install --upgrade pip flask mysql-connector-python

EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
