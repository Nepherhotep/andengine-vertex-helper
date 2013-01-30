import os
import sys



includefiles = []
for d in ('sprites', ):
    for f in os.listdir(d):
        includefile = os.path.join(d, f)
        includefiles.append(includefile)


base = None
name = "AndengineVertexHelper"
version="0.4.1"
author='Alexey Zankevich'
description="Vertex helper for Andengine framework"
author_email='alex.zankevich@gmail.com'
if sys.platform == "win32":
    base = "Win32GUI"
    from cx_Freeze import setup, Executable
    setup(name=name,
      version=version,
      description=description,
	  author=author,
	  author_email=author_email,
      packages=['vertex_helper'],
      options = {'build_exe': {'excludes':[],
                               'packages':[],
                               'include_files':includefiles}}, 
      executables = [Executable("avhelper.pyw",
                                base=base,
                                shortcutDir='ProgramMenuFolder',
                                shortcutName='avhelper')])
else:
    from distutils.core import setup
    setup(name=name,
      version=version,
      description=description,
      author=author,
      author_email=author_email,
      packages=['vertex_helper'],
      scripts=['avhelper.pyw'])
	
        
