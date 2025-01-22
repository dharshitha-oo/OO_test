# -*- coding: utf-8 -*-

#linux
FROM python:3.12.3

WORKDIR /app

#FROM public.ecr.aws/lambda/python:3.12

# Copy function code
#COPY app.py ${LAMBDA_TASK_ROOT}

#COPY requirements.txt requirements.txt

RUN pip install uv
RUN uv pip install --system langflow==1.0.19

# Copy the requirements file into the Docker image
COPY requirements.txt requirements.txt

RUN pip install huggingface_hub 
RUN pip install google-api-python-client>=2.130.0

RUN pip install -r requirements.txt
#RUN pip install huggingface_hub==0.23.2 --no-deps \
#    && pip install langflow==1.1.1 --no-deps \
 #   && pip install google-api-python-client>=2.130.0

COPY custom /usr/local/lib/python3.12/site-packages/langflow/custom
COPY . /app

EXPOSE 8080

CMD ["python",  "app.py"]




