#!/usr/bin/env python 
import struct
# magic = b'\xcf\xfa\xed\xfe'
# decoded = struct.unpack('<I', magic)[0]
# print(hex(decoded))

f = open("./lcj.ept", "rb")
try:
    byte = f.read(2+4*11+1+4*2)
    # while byte != "":
    decoded = struct.unpack('<HIIIIIIIIIII?II', byte)
    print(hex(decoded[0]))
    print(hex(decoded[1]))
    print(hex(decoded[2]))
    print(hex(decoded[3]))
    # 
      # ReadInteger(FLeftMargin);
      # ReadInteger(FTopMargin);
      # ReadInteger(FRightMargin);
      # ReadInteger(FBottomMargin);
    print(decoded[4])
    print(decoded[5])
    print(decoded[6])
    print(decoded[7])

    print(decoded[8])
    print(decoded[9])
    print(decoded[10])
    print(decoded[11])

      # ReadBoolean(FNewTable);
      # ReadInteger(FDataLine);
      # ReadInteger(FTablePerPage);
    print(decoded[12])
    print(decoded[13])
    print(decoded[14])
    
    # print(byte)
finally:
    f.close()