openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 \
  -nodes -out files/node_exporter.crt -keyout files/node_exporter.key