import serial
import traceback
import json
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), 'JST')

try:
  port = serial.Serial("/dev/ttyS0",baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,timeout=1.0)
  with port as p:
    while 1:
      result = p.write(b"\xff\x01\x86\x00\x00\x00\x00\x00\x79")
      s = p.read(9)
      if len(s) >= 4 and s[0] == 0xff and s[1] == 0x86:
        print(json.dumps(
            {
                "time": (datetime.now(JST).strftime('%Y-%m-%dT%H:%M:%S %z')),
                "co2": str(s[2]*256 + s[3])
            }))
      break
except:
  traceback.print_exc()
