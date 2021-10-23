FROM python:3.9

RUN echo "Asia/Shanghai" > /etc/timezone \
 && rm /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

ENV PYTHONPATH=/app

COPY requirements.txt /app/
RUN pip install --upgrade pip \
 && pip install wheel \
 && pip install -r /app/requirements.txt \
 && rm -rf ~/.cache/pip

COPY gunicorn_logger.py run.py run_worker.py /app/
COPY samurai /app/samurai/

EXPOSE 1112

CMD ["gunicorn", "-b", "0.0.0.0:1112", "samurai.app:app"]
