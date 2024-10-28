FROM python:3.12.7-slim

# Install `pip` and needed Python packages from `requirements.txt`
COPY requirements.txt /
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

# Set up an app directory for your code
COPY . /app
WORKDIR /app

EXPOSE 8080

# final configuration
CMD ["gunicorn","--config", "gunicorn.conf.py", "app:app"]