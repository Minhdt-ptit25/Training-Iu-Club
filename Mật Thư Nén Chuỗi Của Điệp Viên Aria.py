def compress_string(s):
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += str(count) + s[i - 1]
            count = 1

    # Thêm ký tự cuối cùng
    result += str(count) + s[-1]
    return result

# Nhập chuỗi thông điệp
n = int(input())
for _ in range(n):
    message = input().strip()
    compressed = compress_string(message)
    print(compressed)
