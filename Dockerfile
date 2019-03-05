# Pull base image
FROM python:3.7-alpine3.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /app
WORKDIR /app

# Install dependencies
RUN apk add --no-cache --virtual \
            git \
            libcurl \
            curl-dev \
            libc-dev \
            pcre-dev \
            postgresql-libs \
            libffi-dev \
    && pip install pipenv \
    # psycopg2 dependencies
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
    && apk add postgresql-client\
    && apk add linux-headers

COPY Pipfile Pipfile.lock ./
RUN pipenv install --dev --system

# Copy project
ADD . ./

RUN chmod +x /app/docker-entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["sh","/app/docker-entrypoint.sh"]
CMD ["dev"]