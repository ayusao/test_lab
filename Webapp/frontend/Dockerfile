FROM python:3.9-slim

WORKDIR /app

COPY ./templates /app/templates

EXPOSE 8000

# Serve the static files using Python's built-in HTTP server
CMD ["python", "-m", "http.server", "8000"]
