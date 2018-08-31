set -x
set -e

gcc -g -I ../rust/target/c/ ../rust/target/debug/libchucknorris.so main.c -o ck
./ck
