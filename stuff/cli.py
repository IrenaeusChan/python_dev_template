import os, sys, signal
import click
from clint.textui import puts, colored

from stuff.version import __version__
#import ch.utils.logger as log

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__)
def cli():
    '''Description.'''
    # to make this script/module behave nicely with unix pipes
    # http://newbebweb.blogspot.com/2012/02/python-head-ioerror-errno-32-broken.html
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

@cli.command('do-something', short_help="Should check a few things and output: Hello World! :D")
@click.option('--debug', '-d', is_flag=True, show_default=True, default=False, required=False, help="Print extra debugging output")
def import_samples( debug):
    """
    Does something...
    """
    #import ch.vdbtools.importer as importer
    #importer.import_samples(samples, sample_duckdb, batch_number, debug, clobber)
    puts(colored.green(f"---> Successfully ran your first CLI script!"))
    puts(colored.green(f"Hello World! :D"))
