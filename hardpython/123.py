import struct
import serial
import time
def checksum_crc8(data):
    crc8_table = [
        0, 94, 188, 226, 97, 63, 221, 131, 194, 156, 126, 32, 163, 253, 31, 65,
        157, 195, 33, 127, 252, 162, 64, 30, 95, 1, 227, 189, 62, 96, 130, 220,
        35, 125, 159, 193, 66, 28, 254, 160, 225, 191, 93, 3, 128, 222, 60, 98,
        190, 224, 2, 92, 223, 129, 99, 61, 124, 34, 192, 158, 29, 67, 161, 255,
        70, 24, 250, 164, 39, 121, 155, 197, 132, 218, 56, 102, 229, 187, 89, 7,
        219, 133, 103, 57, 186, 228, 6, 88, 25, 71, 165, 251, 120, 38, 196, 154,
        101, 59, 217, 135, 4, 90, 184, 230, 167, 249, 27, 69, 198, 152, 122, 36,
        248, 166, 68, 26, 153, 199, 37, 123, 58, 100, 134, 216, 91, 5, 231, 185,
        140, 210, 48, 110, 237, 179, 81, 15, 78, 16, 242, 172, 47, 113, 147, 205,
        17, 79, 173, 243, 112, 46, 204, 146, 211, 141, 111, 49, 178, 236, 14, 80,
        175, 241, 19, 77, 206, 144, 114, 44, 109, 51, 209, 143, 12, 82, 176, 238,
        50, 108, 142, 208, 83, 13, 239, 177, 240, 174, 76, 18, 145, 207, 45, 115,
        202, 148, 118, 40, 171, 245, 23, 73, 8, 86, 180, 234, 105, 55, 213, 139,
        87, 9, 235, 181, 54, 104, 138, 212, 149, 203, 41, 119, 244, 170, 72, 22,
        233, 183, 85, 11, 136, 214, 52, 106, 43, 117, 151, 201, 74, 20, 246, 168,
        116, 42, 200, 150, 21, 75, 169, 247, 182, 232, 10, 84, 215, 137, 107, 53
    ]

    check = 0
    for i in range (2,len(data)):
        a=data[i]
        check = crc8_table[check ^ a]

    return check & 0x00FF

def Baseon(vx,vy,raw):
    data_head="AA 55 0A 11 00 03"
    data=[0xAA,0x55]
    vx_str = struct.pack('>f' ,float(vx)).hex()
    vy_str = struct.pack('>f' ,float(vy)).hex()
    raw_str = struct.pack('>f' ,float(raw)).hex()
    send_data=data_head + "01"+vx_str +"02"+vy_str+"03"+raw_str
    print(send_data)
    send_data = send_data.replace(" ", "").upper()
    send_databyte=bytes.fromhex(send_data)
    crc=checksum_crc8(send_databyte)
    for i in range (2,len(send_databyte)):
        data.append(send_databyte[i])
    data.append(crc)
    print(data)
    #com.write(data)
    for i in data:
        print(hex(i),end=" ")
def Baseoff():
    data=[0xAA,0x55,0x0A,0x01,0x05,0x91]
    #com.write(data)
if __name__ == "__main__":
    #com = serial.Serial('COM8', 1000000)
    data=[170,0x55,0x02,0x08,0x78,0x05,0x64,0x00,0x64,0x00,0x05,0x00,0xf0]
    #com.write(bytes.fromhex("AA 55 02 08 78 05 64 00 64 00 05 00 F0"))
    #com.write(data)
    Baseon(2.0,-1.0,2.0)
    time.sleep(1)
    Baseoff()  #底盘停止