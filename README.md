# NS_project2

- python 2.7

## Env

```bash
# Same command as Remote (Ubuntu 18.04) and Local (macOS 10.12.6)
python2 -V
virtualenv venv --python=python2
. venv/bin/activate
python -V
pip install -r requirements.txt
```

## Build

```bash
# Ubuntu
# GCC can't compile 32bits (-m32) by default, install this
sudo apt-get install gcc-multilib
gcc -o a.out main.c -m32 -fno-stack-protector -g
./a.out
objdump -d -M intel a.out > ./b.dump

# macOS
gcc -o a.out main.c -m32 -fno-stack-protector -g
./a.out
```

## Refs

- http://docs.pwntools.com/en/stable/context.html#pwnlib.context.ContextType.architectures
