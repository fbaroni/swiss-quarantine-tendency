FROM python:3
WORKDIR /
# Run your commands
RUN pwd && ls -l
RUN pip install numpy pandas Flask
COPY . /
CMD [ "python", "./read_file.py" ]