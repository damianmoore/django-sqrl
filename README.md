# django-sqrl

This is very much a not-yet-functioning work-in-progress implementation of SQRL
for Django.



You will need Pillow or PIL to generate the QR Codes. On most systems this will
compile C extensions and requires the Python development and ZLIB libraries. On
Debian-based systems you should run the following first if you want to use the
packaged versions

  apt-get install python-dev zlib1g-dev

You can then for example install Pillow with the following:

  pip install Pillow

At the end of the installation summary make sure you see the line
"ZLIB (PNG/ZIP) support available".



You will also need the C library 'libsodium' and the Python wrapper for it
'pysodium'.

Download libsodium

  ./configure
  make
  sudo make install
  sudo ldconfig

  pip install pysodium
