# -*- mode: python -*-

block_cipher = None


a = Analysis(['Ex3-Tracker.py'],
             pathex=['/Users/ast/Erik/ex-3e-init-tracker'],
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
          upx=True,
          console=False )
app = BUNDLE(exe,
         name='Ex3-Tracker.app',
         icon=None,
         bundle_identifier=None,
         info_plist={
            'NSHighResolutionCapable': 'True'
            },
         )
