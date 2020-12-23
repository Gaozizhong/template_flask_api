FROM python
WORKDIR /home/achievement_display_flask_api

COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

COPY . .

CMD ["gunicorn", "starter:app", "-c", "./gunicorn.conf.py"]
