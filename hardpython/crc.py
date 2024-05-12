
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
data_head="AA 55 0A 0E 00"
vx=0.0
vy=0.0
raw=0.0
vx_str = vx.hex()
vy_str = vy.hex()
raw_str = raw.hex()
send_data=data_head + vx_str + vy_str+raw_str
print(vy_str)
print(send_data)
def find_packets(data, start_marker, end_marker):
    packets = []  # 存储找到的数据包
    start_index = 0  # 开始搜索的位置

    while True:
        # 查找起始标记
        start_index = data.find(start_marker, start_index)
        if start_index == -1:
            break  # 如果没有找到，结束循环

        # 查找结束标记
        end_index = data.find(end_marker, start_index)
        if end_index == -1:
            break  # 如果没有找到，结束循环

        # 提取数据包（包括结束标记）
        packet = data[start_index:end_index + len(end_marker)]
        packets.append(packet)

        # 更新开始搜索的位置
        start_index = end_index + len(end_marker)

    return packets


#
# 给定的十六进制数据
hex_data = "53 59 81 05 00 05 63 4B 42 8F E2 98 54 43"

# 替换空格并转换为大写，以匹配十六进制格式
formatted_hex_data = hex_data.replace(" ", "").upper()

# 调用函数查找数据包
packets = find_packets(formatted_hex_data, "5359", "5443")

# 打印结果
for packet in packets:
    print(packet)
    print(f"Found packet: {packet}")
# ser.close()  # 关闭串口
# if ser.isOpen():  # 判断串口是否关闭
#     print("串口未关闭")
# else:
#     print("串口已关闭")

