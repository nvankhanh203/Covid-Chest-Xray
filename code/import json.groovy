import json

# Dữ liệu đầu vào là chuỗi JSON HỢP LỆ
input_str = '[{"dx":0,"dy":-24,"icon":14115},{"dx":-11,"dy":1,"icon":2955},{"dx":-8,"dy":-24,"icon":14116},{"dx":-7,"dy":-23,"icon":14115},{"dx":-10,"dy":-23,"icon":14114},{"dx":-7,"dy":-24,"icon":14113},{"dx":-9,"dy":-25,"icon":14112},{"dx":-12,"dy":-30,"icon":14116},{"dx":-12,"dy":-32,"icon":14114},{"dx":0,"dy":0,"icon":2955},{"dx":0,"dy":0,"icon":2955},{"dx":0,"dy":0,"icon":2955},{"dx":0,"dy":0,"icon":2955},{"dx":0,"dy":0,"icon":2955}]'

# Parse chuỗi JSON thành danh sách dict
data = json.loads(input_str)

# Chuyển từng dict sang list [icon, dx, dy]
converted = [[item["icon"], item["dx"], item["dy"]] for item in data]

# In kết quả
print(converted)
