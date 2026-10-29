import re, zlib, struct, sys

path = 'Assets/Models/low-poly-hand-painted-dungeon-arch/source/dungeon_arch.fbx'
d = open(path, 'rb').read()

# crude: collect printable strings
strs = [m.group().decode('latin-1') for m in re.finditer(rb'[ -~]{3,}', d)]
uniq = list(dict.fromkeys(strs))
print("=== strings containing tga/png/jpg or trailing .tga ===")
for s in uniq:
    if re.search(r'\.(tga|png|jpg|jpeg|tif|dds)$', s, re.I):
        print(repr(s))

print("\n=== 'Material::' style ===")
for s in uniq:
    if 'Material' in s and '::' in s:
        print(repr(s))

print("\n=== shader / ShaderFX props ===")
for s in uniq:
    if s.startswith('Maya|') or 'ShadingModel' in s or 'Shader' in s:
        print(repr(s))

# Count Material nodes roughly by CBOR header search for 'Material'
print("\n=== count of 'FbxFileTexture' and 'Material' occurrences ===")
print('FbxFileTexture', d.count(b'FbxFileTexture'))
print('FbxSurfaceMaterial', d.count(b'FbxSurfaceMaterial'))
