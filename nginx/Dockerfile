FROM nginx

MAINTAINER Andreas Trawoeger "atrawog@hexaplant.com"

VOLUME ["/var/cache/nginx"]
VOLUME ["/var/log/nginx"]
VOLUME ["/etc/nginx/conf.d"]
VOLUME [" /usr/share/nginx/html"]

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]

