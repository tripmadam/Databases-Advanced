# image
FROM python:3.7-alpine 
WORKDIR /code
#RUN apt install python3-pip
COPY requirements.txt requirements.txt
COPY webscraper.py webscraper.py
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["python3","webscraper.py"]