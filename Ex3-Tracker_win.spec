# -*- mode: python -*-

block_cipher = None


a = Analysis(['Ex3-Tracker.py'],
             pathex=['C:\\Users\\Primefactorx01\\Documents\\Python\\ex-3e-init-tracker'],
             binaries=[],
             datas=[],
             hiddenimports=['queue'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Ex3-Tracker',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=False )
