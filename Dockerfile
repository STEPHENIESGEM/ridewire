FROM python:3.11-slim

WORKDIR /app

# Copy only what's needed for installs first for better cache
COPY requirements-fixed.txt ./requirements-fixed.txt
COPY requirements-lock.txt ./requirements-lock.txt

RUN python -m pip install --upgrade pip setuptools wheel \
    && pip install -r requirements-fixed.txt || pip install -r requirements-lock.txt

# Copy project files
COPY . /app

EXPOSE 8888

CMD ["python", "-m", "jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
