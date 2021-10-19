FROM python:3.8

RUN pip install git+https://github.com/Martis6/calc_project.git

CMD [ "python" ]
