FROM python:3.10

ENV API_ID=14802436
ENV API_HASH=fa2bb567a8b45c564ac4d7f6f75bdb3d
ENV REDIS_URI=redis-17562.c295.ap-southeast-1-1.ec2.cloud.redislabs.com:17562
ENV REDIS_PASSWORD=D9Ik4F1PenE7MvpZ9NL8jk6bflT9XOn8
ENV SESSION=BQFYfdEAGud7n9cE0jh3DbRUDLHoj80P-PJWfTcNl6ASKueJ-Tx39rZrUIIbB2oMTZBF9t5BVcjO4p71vx_2YTWC74cYQPRIydC1FbFrUbH-__rIRI0mhcmc4pW_uW2rh-D0pzy9cMtKnOvs4R0NaA7rlhf6C16_QUcaaPIDtH0rc6Pyzz-ICVnVk2Ka-M2rGEu6oZVwvEh6YmfJZXdNFPw6ybw9dm0PXLAlOauiO8Ke3Lzd76K2t2JmGh0uH3lIh3t5O_BUXzszO8cS3aQqvOnMruHveoiZYWAGbUph3KXdpMFFrwG3PQIOIFe1CD8cmZ5jGsGvFWSbvtnJwGB8S3Xp7AGdGwAAAAA5UcMWAA

RUN apt update && apt upgrade -y; apt-get install git curl zip neofetch ffmpeg -y\
    && apt-get install -y --no-install-recommends ffmpeg neofetch \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/
COPY . /app/

RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

# start the bot.
CMD ["bash", "startup"]
