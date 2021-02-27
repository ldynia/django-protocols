FROM python:3.7.9-slim

ARG PORT=8080
ENV PORT=$PORT

ENV PYTHONUNBUFFERED=True
ENV PYTHONIOENCODING=UTF-8

WORKDIR /app
COPY . /app

RUN apt update && apt install -y \
    curl \
    iproute2 \
    watch

# Fixed permissions, create exec:exec and dev:dev
RUN sed -i '/999/d;' /etc/group && \
    addgroup --system -gid 999 exec && \
    adduser --system --uid 999 --ingroup exec exec && \
    adduser --no-create-home --disabled-password --gecos "" dev && \
    usermod -aG dev exec

RUN chown -R exec:dev \
    /app \
    /usr/local/bin/ \
    /usr/local/lib/python3.7/
RUN chmod -R a-w /etc

EXPOSE ${PORT}
VOLUME /app

HEALTHCHECK CMD curl -f http://localhost:${PORT}/ || exit 1

USER exec:dev

ENTRYPOINT ["/app/scripts/startup.sh"]