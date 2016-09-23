FROM python:3.5
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH $PYTHONPATH:/code:/code/example
ENV DATABASE_NAME postgres
ENV DATABASE_USER postgres
ENV DATABASE_HOST db
ENV DATABASE_PORT 5432
RUN mkdir /code
WORKDIR /code
ADD requirements_dev.txt /code/
RUN pip install -r requirements_dev.txt
ADD . /code/
RUN python setup.py develop
