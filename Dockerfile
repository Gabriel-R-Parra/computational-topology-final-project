FROM python:3.12

ARG USER_UID
ARG USER_NAME

RUN groupadd --gid $USER_UID $USER_NAME && useradd --no-log-init -m --uid $USER_UID --gid $USER_NAME $USER_NAME

COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

USER $USER_NAME
WORKDIR /home/${USER_NAME}/jupyter
