FROM python:3-alpine
COPY app /
RUN mkdir data
WORKDIR /data
RUN touch datafile.txt
RUN chmod 666 datafile.txt
CMD ["/app"]
