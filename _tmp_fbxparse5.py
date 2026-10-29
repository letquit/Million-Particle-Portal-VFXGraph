import re
path = 'Assets/Models/low-poly-hand-painted-dungeon-arch/source/dungeon_arch.fbx'
d = open(path, 'rb').read()
strs = [m.group().decode('latin-1') for m in re.finditer(rb'[ -~]{3,}', d)]
uniq = list(dict.fromkeys(strs))
# candidate object names: strings that look like identifiers near 'Material' nodes
print("=== strings between index 1126 and 1220 ===")
for i in range(1126, 1230):
    if i < len(uniq):
        print(i, repr(uniq[i]))
