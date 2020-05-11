FROM fluent/fluent-bit:1.4

RUN apt-get install -y python3 python3-pip python3-distutils
RUN pip3 install pyserial
COPY fluent-bit.conf fluent-bit/etc/
COPY parsers.conf     fluent-bit/etc/
COPY check_co2.py .
