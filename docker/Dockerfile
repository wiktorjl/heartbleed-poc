FROM ubuntu:trusty

RUN apt-get update
RUN apt-get -y install python python-dev wget curl
RUN apt-get -y install build-essential libffi-dev zlib1g-dev ca-certificates

# Get Ubuntu trusty version of OpenSSL & libssl from Debian snapshots
RUN wget http://snapshot.debian.org/archive/debian/20140106T220635Z/pool/main/o/openssl/openssl_1.0.1f-1_amd64.deb -O /tmp/openssl_1.0.1f-1_amd64.deb
RUN wget http://snapshot.debian.org/archive/debian/20140106T220635Z/pool/main/o/openssl/libssl1.0.0_1.0.1f-1_amd64.deb -O /tmp/libssl1.0.0_1.0.1f-1_amd64.deb
RUN wget http://snapshot.debian.org/archive/debian/20140106T220635Z/pool/main/o/openssl/libssl-dev_1.0.1f-1_amd64.deb -O /tmp/libssl-dev_1.0.1f-1_amd64.deb

# Install these versions of OpenSSL
RUN dpkg -i /tmp/libssl1.0.0_1.0.1f-1_amd64.deb
RUN dpkg -i /tmp/openssl_1.0.1f-1_amd64.deb
RUN dpkg -i /tmp/libssl-dev_1.0.1f-1_amd64.deb

# Adds the snakeoil self signed certificate
RUN apt-get -y install ssl-cert

# Install apache and wsgi to host the Flask app
RUN apt-get -y install apache2 libapache2-mod-wsgi vim

# Create app directories
RUN mkdir -p /var/www/flask

# Copy application files
COPY scripts/memory_leaker.py /usr/local/bin/
COPY scripts/user_simulator.py /usr/local/bin/
COPY scripts/startup.sh /usr/local/bin/
COPY app/flask.py /var/www/flask/
COPY app/app.py /var/www/flask/
COPY app/wsgi.py /var/www/flask/
COPY config/flask.conf /etc/apache2/sites-available/
COPY config/flask-ssl.conf /etc/apache2/sites-available/

# Make scripts executable
RUN chmod +x /usr/local/bin/memory_leaker.py
RUN chmod +x /usr/local/bin/user_simulator.py
RUN chmod +x /usr/local/bin/startup.sh

# Fix permissions
RUN chown -R www-data:www-data /var/www/flask

# Enable Apache modules
RUN a2enmod wsgi ssl rewrite

# Enable our sites
RUN a2dissite 000-default default-ssl
RUN a2ensite flask flask-ssl

EXPOSE 80 443

# Use our startup script
CMD ["/usr/local/bin/startup.sh"]