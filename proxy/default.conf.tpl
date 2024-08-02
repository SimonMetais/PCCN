server {
    listen ${LISTEN_PORT};
    server_name poneys-chevaux-chez-nous.fr www.poneys-chevaux-chez-nous.fr;

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