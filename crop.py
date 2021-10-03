from PIL import Image

def crop(image, frame):
    """
    image 是一个 Image 对象
    frame 是一个 tuple 如下 (x, y, w, h)
        用于表示一个矩形的左上角座标 x y 和 宽高 w h

    不修改原图像
    返回一个 Image 对象, 它是用 frame 把 image 裁剪出来的新图像
    """
    x = frame[0]
    y = frame[1]
    w = frame[2]
    h = frame[3]

    img = Image.new('RGBA', (w, h))
    for i in range(x, x + w):
        for j in range(y, y + h):
            position = (i, j)
            r, g, b, a = image.getpixel(position)
            img.putpixel((i-x, j-y), (r, g, b, a))
    return img

frame = [0, 0, 500, 570]
img = Image.open('spider.png')
img = img.convert('RGBA')
img = crop(img, frame)
img.save('spider.png')