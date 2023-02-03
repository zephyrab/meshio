import src.meshio as meshio

fpath = r"tests\meshes\abaqus\bone_mesh.inp"

mesh = meshio.read(fpath)
