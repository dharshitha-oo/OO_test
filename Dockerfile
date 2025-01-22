# -*- coding: utf-8 -*-

#linux
FROM python:3.12.3

WORKDIR /app



RUN pip install flask


COPY . /app

EXPOSE 8080

CMD ["python",  "app.py"]




