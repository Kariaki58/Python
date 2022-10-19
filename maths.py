import qrcode
data = 'https://www.youtube.com/watch?v=SqvVm3QiQVk&t=3192s'
img = qrcode.make(data)
img.save('./Knowledge.png')
