# https://github.com/dockerfile/nginx/blob/master/Dockerfile
# https://www.digitalocean.com/community/tutorials/docker-explained-how-to-containerize-and-use-nginx-as-a-proxy

FROM openmarble/arch-vips:latest
MAINTAINER Andreas Trawöger <atrawog@openmarble.org>

RUN  pacman --noconfirm -Syu apache mod_fcgid && \
        pacman -Sc --noconfirm

RUN cd /code && \
        git clone https://github.com/ruven/iipsrv.git && \
        cd iipsrv && \
        ./autogen.sh && \
        ./configure && \
        make && \
        mkdir -p /usr/local/iipsrv/ && \
        cp src/iipsrv.fcgi  /usr/local/iipsrv/ && \
        chown -R http.http /usr/local/iipsrv


RUN mkdir -p /config /data /log 
RUN chown -R http.http /data /log
#ADD config/apache2.conf  /etc/apache2/apache2.conf 
#ADD config/iipsrv.conf  /etc/apache2/mods-available/iipsrv.conf
#ADD config/iipsrv.load  /etc/apache2/mods-available/iipsrv.load
#ADD config/ssl.conf  /etc/apache2/mods-available/ssl.conf
ADD config/httpd.conf /etc/httpd/conf/httpd.conf

EXPOSE 80

CMD ["rm", "-f", "/run/apache2/apache2.pid",";","/usr/sbin/apachectl", "-D", "FOREGROUND"]
