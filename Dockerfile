FROM python

ADD . /opt/counter
WORKDIR /opt/counter

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]