FROM node:8-alpine

ADD startup.sh /
ADD package.json /
ADD package-lock.json /

RUN npm install

WORKDIR /apps/app

CMD /startup.sh
