FROM node:18


WORKDIR /meow
COPY package.json .
RUN npm install
COPY . .
CMD npm run dev

