import re
path = 'Assets/Models/low-poly-hand-painted-dungeon-arch/source/dungeon_arch.fbx'
d = open(path, 'rb').read()
strs = [m.group().decode('latin-1') for m in re.finditer(rb'[ -~]{3,}', d)]
uniq = list(dict.fromkeys(strs))
for i in range(880, 1000):
    if i < len(uniq):
        print(i, repr(uniq[i]))
