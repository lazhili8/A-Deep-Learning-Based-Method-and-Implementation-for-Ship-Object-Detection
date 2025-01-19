# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['yolo.py','base_ui.py','main_window.py','camera_show.py','get_map.py','kmeans_for_anchors.py','groundTruth.py','kmeans_for_anchors.py','login.py','main_window.py','predict.py','predict_camera.py','predict_video.py','video_show.py','voc_annotation.py'],
    pathex=[],
    binaries=[],
    datas=[('VOCdevkit','VOCdevkit'), ('video', 'video'),('background.png', '.'),],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='yolo',
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
