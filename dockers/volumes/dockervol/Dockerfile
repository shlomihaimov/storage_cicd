FROM python:3-alpine
COPY app /
RUN mkdir data
RUN chmod 666 /data
WORKDIR /data
CMD ["/app"]
