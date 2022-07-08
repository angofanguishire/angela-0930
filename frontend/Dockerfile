FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./textbox.py /code/

EXPOSE 10101

CMD ["wave", "run", "textbox"]