FROM python:3.10.5

EXPOSE 8000
WORKDIR /aline_capocci

ADD requirements.txt /aline_capocci/

RUN pip install -r requirements.txt

ADD ./blog /aline_capocci

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "--reload", "aline_capocci.wsgi:application"]