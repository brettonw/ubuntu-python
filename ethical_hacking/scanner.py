#! /usr/bin/env python

import nmap
import sys

nmScan = nmap.PortScanner()

nmScanner = nmScan.scan ("192.168.128.10", '80', arguments=' -O')

