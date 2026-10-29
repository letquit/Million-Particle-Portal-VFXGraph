import re
path = 'Assets/Models/low-poly-hand-painted-dungeon-arch/source/dungeon_arch.fbx'
d = open(path, 'rb').read()
strs = [m.group().decode('latin-1') for m in re.finditer(rb'[ -~]{3,}', d)]
uniq = list(dict.fromkeys(strs))
print("total unique strings:", len(uniq))
print("---- all (indexed) ----")
for i, s in enumerate(uniq):
    print(i, repr(s))
