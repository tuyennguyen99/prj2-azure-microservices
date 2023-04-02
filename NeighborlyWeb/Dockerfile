# To enable ssh & remote debugging on app service change the base image to the one below
FROM python:3.8.0

# copy the requirements file into the image
COPY requirements.txt app/

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip3 install -r requirements.txt

# copy every content from the local file to the image
COPY . /app
EXPOSE 80
# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

CMD ["app.py", "--verbose"]