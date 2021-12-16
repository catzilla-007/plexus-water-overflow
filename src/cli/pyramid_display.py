import click

from src.core.glass_pyramid import GlassPyramid


class PyramidDisplay(object):
    def __init__(self, pyramid: GlassPyramid):
        self._pyramid = pyramid

    def display(self):
        height = self._get_pyramid_height()

        space = height - 1

        for i in range(0, height):
            for j in range(0, space):
                click.echo('         ', nl=False)
            space = space - 1

            for j in range(0, i + 1):
                glass_info = self._get_glass_info(i, j)
                click.echo(f'{glass_info}      ', nl=False)

            click.echo('\n', nl=True)

    def _get_glass_info(self, i: int, j: int) -> str:
        glass = self._pyramid.get_glass(i, j)
        return f'[({i},{j}) {glass.content} ml]'

    def _get_pyramid_height(self):
        keys = list(self._pyramid.glasses)
        height = list(map(lambda a: a[0], keys))
        return max(height)
