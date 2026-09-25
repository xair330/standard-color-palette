# -*- coding: utf-8 -*-
"""
标准色彩库极简快捷入口
用法:
    import palette
    from palette import C, Roles, Harmonies
"""

from standard_color_palette import (
    VERSION,
    LOCKED,
    Colors,
    C,
    Harmonies,
    Roles,
    set_mode,
    get_mode,
    apply_style,
    export_json,
    export_css
)

__all__ = [
    "VERSION",
    "LOCKED",
    "Colors",
    "C",
    "Harmonies",
    "Roles",
    "set_mode",
    "get_mode",
    "apply_style",
    "export_json",
    "export_css"
]
