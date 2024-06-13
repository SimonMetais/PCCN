FROM nginx

ENV APP_HOST=PCCV__app
ENV APP_PORT=8000
ENV LISTEN_PORT=81

COPY ./start.sh /start.sh
RUN ["chmod", "+x", "/start.sh"]

RUN ["touch", "/etc/nginx/conf.d/default.conf"]
COPY ./proxy_params /etc/nginx/
COPY ./default.conf.tpl /etc/nginx/

EXPOSE 81

ENTRYPOINT ["sh", "-c", "/start.sh"]