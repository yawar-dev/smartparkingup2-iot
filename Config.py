import os.path


# Replace /Users/yawar-dev/python_certificates with the path
# in which you saved the certificate authority file,
# the client certificate file and the client key
certificates_path = "/Users/yawar-dev/python_certificates"
ca_certificate = os.path.join(certificates_path, "ca.crt")
client_certificate = os.path.join(certificates_path, "board001.crt")
client_key = os.path.join(certificates_path, "board001.key")
# Replace "200.168.1.52" with the IP or hostname for the Mosquitto
# or other MQTT server
# Make sure the IP or hostname matches the value 
# you used for Common Name
mqtt_server_host = "200.168.1.52"
mqtt_server_port = 8883
mqtt_keepalive = 60
