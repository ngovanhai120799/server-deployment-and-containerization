FROM python:3.9-alpine3.19

# Set up an app directory for your code
COPY . /app
WORKDIR /app

# Install `pip` and needed Python packages from `requirements.txt`
COPY requirements.txt /
RUN pip3 install --upgrade pip gunicorn
RUN pip3 install -r /requirements.txt

# final configuration
CMD ["gunicorn", "-b", ":8080", "app:app"]