#https://hackerone.com/reports/213261
git clone https://github.com/mruby/mruby.git
cd mruby
git reset –hard 4cf38eb9032ab70544f940941703a0c09529539f
make CC=vcc CXX=v++ CFLAGS="-fPIE" LD=vcc
# ASAN Build:
# CC=clang CXX=clang++  LDFLAGS="-fsanitize=address" CFLAGS="-fPIE -fsanitize=address -g" make -j`nproc`
