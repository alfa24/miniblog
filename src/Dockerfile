FROM python:3.6-stretch

# Set the file maintainer (your name - the file's author)
MAINTAINER Falichev Aleksandr

# Set env variables used in this Dockerfile (add a unique prefix, such as DOCKYARD)
# Local directory with project source
ENV DOCKYARD_SRC=code/django_app
# Directory in container for all project files
ENV DOCKYARD_SRVHOME=/srv
# Directory in container for project source files
ENV DOCKYARD_SRVPROJ=$DOCKYARD_SRVHOME/$DOCKYARD_SRC

WORKDIR $DOCKYARD_SRVHOME
RUN mkdir static
#read
VOLUME ["$DOCKYARD_SRVPROJ/static/"]

# Update the default application repository sources list
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y git
RUN apt-get install -y vim
RUN apt-get install -y nginx

# Create application subdirectories
WORKDIR $DOCKYARD_SRVPROJ
# Copy application source code to SRCDIR
COPY . $DOCKYARD_SRVPROJ
# Install Python dependencies
RUN pip install -r $DOCKYARD_SRVPROJ/requirements.txt

# expose the port 8000
EXPOSE 8000
EXPOSE 443
EXPOSE 80

# Copy entrypoint script into the image
WORKDIR $DOCKYARD_SRVPROJ
COPY ./docker-django-entrypoint.sh /
COPY ./docker-celery-entrypoint.sh /
COPY ./config/nginx/conf.d/django_nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/django_nginx.conf /etc/nginx/sites-enabled/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
