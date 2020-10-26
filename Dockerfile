FROM python:3-slim
ENV APP_NAME="app-intro"
ENV APP_DIR="/opt/${APP_NAME}"
ENV PROJ_NAME="form"

RUN mkdir ${APP_DIR}
WORKDIR ${APP_DIR}
COPY app/requirements.txt ${APP_DIR}
RUN pip install -r requirements.txt
COPY app/. ${APP_DIR}/

EXPOSE 8000
USER nobody
CMD ["python3","/opt/app-intro/manage.py","runserver","0.0.0.0:8000"]