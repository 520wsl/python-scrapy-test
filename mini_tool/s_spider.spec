# -*- mode: python -*-

block_cipher = None


a = Analysis(['s_spider.py'],
             pathex=['E:\\GIT\\python-scrapy-test\\mini_tool'],
             binaries=[],
             datas=[
                ('scrapy','scrapy'),
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
          name='MiniTool',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='6.ico')
