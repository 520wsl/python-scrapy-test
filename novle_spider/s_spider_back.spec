# -*- mode: python -*-

block_cipher = None


a = Analysis(['s_spider.py'],
             pathex=['E:\\GIT\\python-scrapy-test\\novle_spider'],
             binaries=[],
             datas=[
                ('scrapy','scrapy'),
                ('novle_spider','novle_spider'),
                ('scrapy.cfg','.'),
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='novle',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='6.ico')

     coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='s_spider')
