from src.water_overflow.glass_pyramid import GlassPyramid


def main():
    pyramid = GlassPyramid(250, 1)
    pyramid.pour()

    glass = pyramid.get_glass(2, 2)
    print(glass.value)


main()
