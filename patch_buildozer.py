import os
import sys
import site
from pathlib import Path


def find_buildozer_init():
    candidates = []
    search_dirs = set()

    try:
        for directory in site.getsitepackages():
            search_dirs.add(Path(directory))
    except Exception:
        pass

    try:
        search_dirs.add(Path(site.getusersitepackages()))
    except Exception:
        pass

    for directory in map(Path, sys.path):
        if directory.exists():
            search_dirs.add(directory)

    for directory in search_dirs:
        path = directory / 'buildozer' / '__init__.py'
        if path.exists():
            candidates.append(path)
    return candidates


def patch_file(path: Path):
    text = path.read_text(encoding='utf-8')
    if 'from urllib.request import FancyURLopener\n' not in text:
        print(f'No direct FancyURLopener import in {path}, no patch needed.')
        return False

    replacement = (
        'try:\n'
        '    from urllib.request import FancyURLopener\n'
        'except ImportError:\n'
        '    from urllib.request import URLopener as FancyURLopener\n'
    )

    if 'try:\n    from urllib.request import FancyURLopener\n' in text:
        print(f'Buildozer already patched in {path}.')
        return False

    new_text = text.replace('from urllib.request import FancyURLopener\n', replacement)
    if new_text == text:
        print(f'No replacement made in {path}.')
        return False

    path.write_text(new_text, encoding='utf-8')
    print(f'Patched {path}')
    return True


def main():
    paths = find_buildozer_init()
    if not paths:
        print('Buildozer __init__.py not found in sys.path. Is buildozer installed?')
        sys.exit(1)

    print('Buildozer __init__.py locations:')
    for path in paths:
        print(f'  - {path}')

    patched_any = False
    for path in paths:
        patched_any |= patch_file(path)

    if not patched_any:
        print('No patches were applied. Buildozer may already be compatible or patch not needed.')
    else:
        print('Patch applied successfully.')


if __name__ == '__main__':
    main()
