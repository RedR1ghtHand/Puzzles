FROM postgres:alpine3.18
ENV POSTGRES_PASSWORD=4aika
ENV POSTGRES_USER=4aika
ENV POSTGRES_DB=database
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql