FROM python:3-slim
RUN mkdir /home/user
COPY app /home/user
WORKDIR /home/user
RUN touch datafile.txt
RUN chmod 666 datafile.txt
RUN chown -R 2021:2021 /home/user
USER 2021
CMD ["python", "app"]
