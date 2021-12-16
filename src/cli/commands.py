import click

from src.core.glass_pyramid import GlassPyramid


@click.command()
@click.option('--liters', default=1, help='set number of liters to pour')
@click.option('--capacity', default=250, help='set glass capacity')
@click.option('--i', default=0, help='the i position of the glass to check')
@click.option('--j', default=0, help='the j position of the glass to check')
def pour(liters, capacity, i, j):
    pyramid = GlassPyramid(capacity, liters)
    pyramid.pour()
    glass = pyramid.get_glass(i, j)
    click.echo(f'content in glass[{i}, {j}]: {glass.content} mL')
