import re

data_str = "success: get_uid\ndata:\n\t[101, 19, 32, 239]\n\t['0x65', '0x13', '0x20', '0xef']\n\te  \n80 4F 0C A0 00 00 03 06 03 00 01 00 00 00 00\n00 01\nCard Name: MIFARE Classic 1K\n\tT0 True\n\tT1 True\n\tT1 False"

match = re.search(r"\[(.*?)\]", data_str)
numbers_str = match.group(1)
numbers = [int(n) for n in numbers_str.split(", ")]
print(numbers)
