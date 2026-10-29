import re
path = 'Assets/Models/low-poly-hand-painted-dungeon-arch/source/dungeon_arch.fbx'
d = open(path, 'rb').read()

# Find Material nodes: FBX binary uses 'Material' node header then properties (u8,name,sub)
# Simpler: look for b'Material::'
print("Literal 'Material::' occurrences:", d.count(b'Material::'))
for m in re.finditer(rb'Material::[ -~]{1,80}', d):
    print(repr(m.group().decode('latin-1')))

print()
print("Literal 'Texture::' occurrences:", d.count(b'Texture::'))
for m in re.finditer(rb'Texture::[ -~]{0,80}', d):
    print(repr(m.group().decode('latin-1')))

print()
print("Literal 'Model::' occurrences:", d.count(b'Model::'))
for m in re.finditer(rb'Model::[ -~]{0,80}', d):
    print(repr(m.group().decode('latin-1')))
