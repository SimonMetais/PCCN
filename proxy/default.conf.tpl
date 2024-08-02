server {
    listen 80;
    server_name poneys-chevaux-chez-nous.fr www.poneys-chevaux-chez-nous.fr;

    location / {
        proxy_pass http://PCCN__app:8000;
        include /etc/nginx/proxy_params;
    }
}