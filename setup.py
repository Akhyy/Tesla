#!/usr/bin/env python3

import subprocess

# Installe pip3
proc = subprocess.Popen('sudo apt-get install -y pip3', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
proc.wait()

# Installe les packages Python nécessaires
packages = [
    'adafruit-circuitpython-hcsr04',
    'adafruit-circuitpython-ina219',
    'adafruit-circuitpython-pca9685',
    'adafruit-circuitpython-servokit',
    'adafruit-circuitpython-tcs34725',
    'Adafruit-GPIO',
    'Adafruit-PCA9685',
    'RPi.GPIO',
    'smbus2'
]

# Mettre à jour les paquets déjà existants
subprocess.call(['sudo', 'apt', 'update'])

# Installer les packages Python via pip
for package in packages:
    subprocess.call(['sudo', 'pip3', 'install', package])