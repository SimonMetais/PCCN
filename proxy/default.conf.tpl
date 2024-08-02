server {
    listen 443 ssl;
    server_name poneys-chevaux-chez-nous.fr www.poneys-chevaux-chez-nous.fr;

    # Chemins vers les certificats
    ssl_certificate /etc/nginx/ssl/certificate.cer;
    ssl_certificate_key /etc/nginx/ssl/private.key;

    # Configuration SSL
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    location /static {
        alias /static;
    }

    location /media {
        alias /media;
    }

    location / {
        proxy_pass http://PCCN__app:8000;
        include /etc/nginx/proxy_params;
    }
}

server {
    listen 80;
    server_name poneys-chevaux-chez-nous.fr www.poneys-chevaux-chez-nous.fr;

    location / {
        return 301 https://$host$request_uri;
    }
}
