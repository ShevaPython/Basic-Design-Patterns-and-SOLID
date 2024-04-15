class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f'Loading image from {filename}')

    def draw(self):
        print(f'Drawing image {self.filename}')


class LazyBitmap:
    """
    Когда вызывается метод draw() у объекта LazyBitmap, он сначала проверяет, загружено ли уже изображение (self.bitmap)
    . Если нет, то создается объект Bitmap с указанным именем файла, и вызывается его метод draw(). Если изображение
    уже было загружено, просто вызывается метод draw() этого изображения.

    Этот механизм позволяет отложить загрузку изображения до тех пор, пока оно действительно не понадобится, что может
    быть полезно, если работа с изображением требует много ресурсов или если изображение используется не всегда.
    """

    def __init__(self, filename):
        self.filename = filename
        self.bitmap = None

    def draw(self):
        if not self.bitmap:
            self.bitmap = Bitmap(self.filename)
        self.bitmap.draw()


def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing image')


if __name__ == '__main__':
    bmp = LazyBitmap('facepalm.jpg')  # Bitmap
    draw_image(bmp)
