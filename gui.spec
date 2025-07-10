# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\dhruv\\OneDrive\\Desktop\\PROJECTS\\Project 3.0\\Real-ESRGAN\\upscaler\\gui.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\dhruv\\OneDrive\\Desktop\\PROJECTS\\Project 3.0\\Real-ESRGAN\\upscaler\\RealESRGAN_x4plus.pth', '.')],
    hiddenimports=['torch', 'basicsr', 'realesrgan', 'cv2'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
