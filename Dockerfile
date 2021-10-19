FROM python:3.8

RUN pip install git+https://github.com/miglegervyte/Calculator.git

CMD [ "python" ]
