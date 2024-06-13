server {
    listen ${LISTEN_PORT};

    location /static {
        alias /static;
    }

    location /media {
        alias /media;
    }

    location / {
        proxy_pass      http://${APP_HOST}:${APP_PORT};
        include         /etc/nginx/proxy_params;
    }
}