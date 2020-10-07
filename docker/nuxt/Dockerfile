# base image
FROM node:14.13.0-stretch

RUN mkdir -p /var/www/webapp

# node.js の環境変数を定義する
# 本番環境では production
ENV NODE_ENV=development

# install modules
RUN yarn install
RUN yarn add @nuxtjs/axios

# ワーキングディレクトリを変更
WORKDIR /code