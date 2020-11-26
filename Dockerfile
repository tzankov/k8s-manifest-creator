FROM alpine:latest
COPY creator/* /home/creator/
COPY requirements.txt /home/creator/requirements.txt
RUN apk add python3
RUN python3 -m ensurepip && pip3 install --upgrade pip && pip3 install -r /home/creator/requirements.txt
CMD python3 /home/creator/creator.py