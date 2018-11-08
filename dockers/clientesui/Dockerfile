FROM node:8

RUN npm install -g @vue/cli && \
    npm install -g @vue/cli-service-global

ADD startup.sh /
WORKDIR /apps/app
CMD /startup.sh