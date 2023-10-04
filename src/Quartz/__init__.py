import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

__version__ = "1.0.0"
__author__ = __maintainer__ = 'clr-cera'

NAME = 'icmchat.ddns.net'
DOMAIN = ''
IP = ''
PORT = 9999
IPTYPE = 'IPV4' # Can be IPV4, IPV6 or CNAME, by default goes to IPV4
VERSION = __version__
