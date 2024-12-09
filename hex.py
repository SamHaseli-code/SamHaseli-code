# ایجاد فایل example.py
with open('example.py', 'w') as file:
    file.write("print('Hello, World!')")





# تبدیل example.py به کد هگز
input_file = 'example.py'

with open(input_file, 'rb') as file:
    file_content = file.read()

hex_code = file_content.hex()

# ذخیره کد هگز در یک فایل
output_file = 'example_hex.txt'
with open(output_file, 'w') as file:
    file.write(hex_code)

print(f'کد هگز فایل {input_file} در فایل {output_file} ذخیره شد.')
