# Start with a base Python 3.7.0 image
FROM python:3.7.0

# Add the external tasks directory into /tasks
WORKDIR /src

ADD locust/requirements.txt .
RUN pip install -r requirements.txt

ADD locust/run.sh .
ADD locust/dummy_loadtest.py .

# Expose the required Locust ports
EXPOSE 5557 5558 8089

# Set script to be executable
RUN chmod 755 run.sh

# Start Locust using LOCUS_OPTS environment variable
CMD ["bash", "run.sh"]
