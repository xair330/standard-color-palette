# -*- coding: utf-8 -*-
"""
标准色彩库 (Standard Color Palette Library)
版本: 1.0.0
受控状态: FROZEN / LOCKED (严禁未经用户显式许可擅自修改)

本库定义了民航统计分析中已通过严格审查的 69 个专业基准色、10 大色彩家族及 6 组经典调和矩阵。
支持点语法自动补全、场景语义调用、经典搭配矩阵调用以及 Matplotlib 绘图样式无感注入。
"""

import json
from types import MappingProxyType
from typing import Dict, List, Tuple, Any

VERSION = "1.0.0"
LOCKED = True
AUTHORIZATION_REQUIRED = True

# =============================================================================
# 1. 色彩原始数据表 (全量 69 色，双模态 Hex 对照)
# =============================================================================

# 格式: KEY: (色彩专业英文名, 低饱和合规Hex, 原始提取Hex, 色彩家族英文, 中文说明)
_COLOR_DEFINITIONS: Dict[str, Tuple[str, str, str, str, str]] = {
    # 家族 1: SLATE & NAVY (板岩海蓝系)
    "SLATE_CHARCOAL": ("SLATE_CHARCOAL", "#5A626A", "#5A626A", "SLATE & NAVY", "板岩炭灰"),
    "PALE_PLATINUM":  ("PALE_PLATINUM",  "#B0B5BA", "#B0B5BA", "SLATE & NAVY", "浅白金灰"),
    "DEEP_NAVY":      ("DEEP_NAVY",      "#596C8A", "#264C8A", "SLATE & NAVY", "深海蓝"),
    "SLATE_BLUE":     ("SLATE_BLUE",     "#778EA5", "#6485A5", "SLATE & NAVY", "板岩蓝"),
    "ICE_AZURE":      ("ICE_AZURE",      "#E6F0F8", "#E6F0F8", "SLATE & NAVY", "冰霜浅青"),
    "FOG_BLUE":       ("FOG_BLUE",       "#D0E2EE", "#D0E2EE", "SLATE & NAVY", "雾蓝"),
    "KHAKI_BUFF":     ("KHAKI_BUFF",     "#CDC293", "#CDBE7B", "SLATE & NAVY", "卡其原沙"),

    # 家族 2: STEEL & OCHRE (钢蓝暖赭系)
    "STEEL_BLUE":     ("STEEL_BLUE",     "#7893B1", "#5B84B1", "STEEL & OCHRE", "钢蓝"),
    "DEEP_TEAL":      ("DEEP_TEAL",      "#5B8080", "#4C8080", "STEEL & OCHRE", "深青"),
    "CINNAMON_BROWN": ("CINNAMON_BROWN", "#BD987A", "#BD7A42", "STEEL & OCHRE", "肉桂褐"),
    "PALE_AQUA":      ("PALE_AQUA",      "#EAF5F2", "#EAF5F2", "STEEL & OCHRE", "苍水绿"),
    "ROSE_MAUVE":     ("ROSE_MAUVE",     "#C8879B", "#C86684", "STEEL & OCHRE", "玫瑰锦葵"),
    "WARM_AMBER":     ("WARM_AMBER",     "#D9AF8D", "#D97F36", "STEEL & OCHRE", "暖琥珀"),
    "GOLDEN_OCHRE":   ("GOLDEN_OCHRE",   "#D9B38D", "#D98835", "STEEL & OCHRE", "金赭黄"),
    "CORAL_TERRA":    ("CORAL_TERRA",    "#D8908C", "#D8554E", "STEEL & OCHRE", "珊瑚红"),
    "MUTED_CRIMSON":  ("MUTED_CRIMSON",  "#C78181", "#C72828", "STEEL & OCHRE", "沉暗红"),

    # 家族 3: MINT & SAGE (薄荷灰绿系)
    "SAGE_GREEN":     ("SAGE_GREEN",     "#81A98F", "#81A98F", "MINT & SAGE", "鼠尾草绿"),
    "CREAM_YELLOW":   ("CREAM_YELLOW",   "#F8E7A2", "#F8E7A2", "MINT & SAGE", "奶油暖黄"),
    "DUSTY_ROSE":     ("DUSTY_ROSE",     "#E8ABA7", "#E8928D", "MINT & SAGE", "灰玫瑰红"),
    "OLIVE_DRAB":     ("OLIVE_DRAB",     "#999063", "#998A3D", "MINT & SAGE", "暗橄榄"),
    "SEA_GREEN":      ("SEA_GREEN",      "#6CA69F", "#6CA69F", "MINT & SAGE", "海碧绿"),
    "PEWTER_GRAY":    ("PEWTER_GRAY",    "#95A1A6", "#95A1A6", "MINT & SAGE", "白蜡冷灰"),
    "PLUM_SLATE":     ("PLUM_SLATE",     "#7C6A89", "#7C6A89", "MINT & SAGE", "灰李紫"),
    "LAVENDER_MIST":  ("LAVENDER_MIST",  "#E8DCE8", "#E8DCE8", "MINT & SAGE", "薰衣草雾"),

    # 家族 4: CELADON & SAND (青瓷暖沙系)
    "CELADON_MINT":   ("CELADON_MINT",   "#82C18E", "#82C18E", "CELADON & SAND", "青瓷绿"),
    "DEEP_MOSS":      ("DEEP_MOSS",      "#56755E", "#56755E", "CELADON & SAND", "深苔绿"),
    "SAND_GOLD":      ("SAND_GOLD",      "#F1DC9C", "#F1CE63", "CELADON & SAND", "沙金黄"),
    "MUSTARD_OCHRE":  ("MUSTARD_OCHRE",  "#E0CA91", "#E0B84C", "CELADON & SAND", "芥末赭"),
    "INDIGO_SLATE":   ("INDIGO_SLATE",   "#7594B4", "#417BB4", "CELADON & SAND", "靛蓝灰"),
    "COPPER_RUST":    ("COPPER_RUST",    "#D8A98C", "#D86B26", "CELADON & SAND", "红铜锈"),
    "BURNT_UMBER":    ("BURNT_UMBER",    "#8E655C", "#8E321E", "CELADON & SAND", "焦褐赭"),

    # 家族 5: JADE & CYAN (翡翠暗青系)
    "JADE_GREEN":     ("JADE_GREEN",     "#77B89A", "#52B889", "JADE & CYAN", "翡翠绿"),
    "DARK_CYAN":      ("DARK_CYAN",      "#4F7B73", "#327B6F", "JADE & CYAN", "暗深青"),
    "COBALT_SLATE":   ("COBALT_SLATE",   "#7082A4", "#5672A4", "JADE & CYAN", "钴蓝灰"),
    "CLOUD_BLUE":     ("CLOUD_BLUE",     "#A4B8CE", "#A4B8CE", "JADE & CYAN", "云水蓝"),
    "AMBER_ORANGE":   ("AMBER_ORANGE",   "#F1C39C", "#F19C52", "JADE & CYAN", "琥珀橙"),
    "APPLE_GREEN":    ("APPLE_GREEN",    "#A8CD96", "#9ACD82", "JADE & CYAN", "嫩苹果绿"),
    "TANGERINE":      ("TANGERINE",      "#F0C29C", "#F08428", "JADE & CYAN", "蜜柑橙"),
    "ESPRESSO_BROWN": ("ESPRESSO_BROWN", "#6E5547", "#6E381A", "JADE & CYAN", "浓缩咖啡褐"),

    # 家族 6: FOREST & BERRY (苍林浆果系)
    "FOREST_GREEN":   ("FOREST_GREEN",   "#719D74", "#609D64", "FOREST & BERRY", "苍林绿"),
    "SUNFLOWER_GOLD": ("SUNFLOWER_GOLD", "#E5CB94", "#E5B242", "FOREST & BERRY", "向日葵金"),
    "CARROT_ORANGE":  ("CARROT_ORANGE",  "#E8BB96", "#E88939", "FOREST & BERRY", "胡萝卜橙"),
    "SAFFRON_YELLOW": ("SAFFRON_YELLOW", "#D9BE8D", "#D9A74A", "FOREST & BERRY", "藏红花黄"),
    "BERRY_MAGENTA":  ("BERRY_MAGENTA",  "#D68BA6", "#D65A88", "FOREST & BERRY", "浆果洋红"),
    "BLUSH_PINK":     ("BLUSH_PINK",     "#F5DDE6", "#F5DDE6", "FOREST & BERRY", "浅颊粉"),
    "HEATHER_PURPLE": ("HEATHER_PURPLE", "#8F6F8E", "#8F6F8E", "FOREST & BERRY", "石楠紫灰"),

    # 家族 7: CADET & BRICK (军灰砖红系)
    "CADET_BLUE":     ("CADET_BLUE",     "#9BB2C9", "#9BB2C9", "CADET & BRICK", "军校灰蓝"),
    "TOPAZ_GOLD":     ("TOPAZ_GOLD",     "#EBC698", "#EBA64E", "CADET & BRICK", "黄玉金"),
    "BRICK_RED":      ("BRICK_RED",      "#C0847C", "#C04838", "CADET & BRICK", "砖石红"),
    "RAW_SIENNA":     ("RAW_SIENNA",     "#DDB992", "#DDA668", "CADET & BRICK", "生赭黄"),
    "GARNET_RED":     ("GARNET_RED",     "#9E6966", "#9E3832", "CADET & BRICK", "深石榴红"),

    # 家族 8: TEAL & SEAFOAM (碧海松青系)
    "PALE_SEAFOAM":   ("PALE_SEAFOAM",   "#BDE8D9", "#BDE8D9", "TEAL & SEAFOAM", "浅海沫青"),
    "TURQUOISE_BLUE": ("TURQUOISE_BLUE", "#87B7C1", "#6BB3C1", "TEAL & SEAFOAM", "绿松石蓝"),
    "PETROL_CYAN":    ("PETROL_CYAN",    "#668F9D", "#32829D", "TEAL & SEAFOAM", "石油蓝青"),
    "MIDNIGHT_NAVY":  ("MIDNIGHT_NAVY",  "#4A5F72", "#1E4B72", "TEAL & SEAFOAM", "午夜藏青"),
    "WHEAT_GOLD":     ("WHEAT_GOLD",     "#D8C792", "#D8BE6E", "TEAL & SEAFOAM", "麦穗金"),
    "PINE_GREEN":     ("PINE_GREEN",     "#689A82", "#689A82", "TEAL & SEAFOAM", "松针绿"),
    "BURNT_ORANGE":   ("BURNT_ORANGE",   "#E8B496", "#E86A22", "TEAL & SEAFOAM", "焦橙"),

    # 家族 9: WILLOW & TERRA (柳绿暖褐系)
    "WILLOW_GREEN":   ("WILLOW_GREEN",   "#8FB89A", "#8FB89A", "WILLOW & TERRA", "柳叶绿"),
    "BARLEY_BUFF":    ("BARLEY_BUFF",    "#DDC39C", "#DDB87E", "WILLOW & TERRA", "大麦原沙"),
    "SALMON_CORAL":   ("SALMON_CORAL",   "#E5ADA4", "#E59688", "WILLOW & TERRA", "鲑鱼珊瑚"),
    "AQUA_SLATE":     ("AQUA_SLATE",     "#89B9B8", "#89B9B8", "WILLOW & TERRA", "水碧灰蓝"),

    # 家族 10: GLACIER & RUBY (冰川红宝石系)
    "GLACIER_MIST":   ("GLACIER_MIST",   "#E6F0F8", "#E6F0F8", "GLACIER & RUBY", "冰川雾青"),
    "CERULEAN_BLUE":  ("CERULEAN_BLUE",  "#8BB6D1", "#64A8D1", "GLACIER & RUBY", "蔚蓝"),
    "SHELL_PINK":     ("SHELL_PINK",     "#FDECEF", "#FDECEF", "GLACIER & RUBY", "贝壳淡粉"),
    "RUBY_CRIMSON":   ("RUBY_CRIMSON",   "#C8828E", "#C83C55", "GLACIER & RUBY", "红宝石深红"),
    "EMERALD_TEAL":   ("EMERALD_TEAL",   "#6FA39C", "#54A399", "GLACIER & RUBY", "祖母绿青"),
    "MARIGOLD_AMBER": ("MARIGOLD_AMBER", "#D4B789", "#D49B3E", "GLACIER & RUBY", "金盏花琥珀"),
    "SCARLET_RED":    ("SCARLET_RED",    "#C47F83", "#C42730", "GLACIER & RUBY", "深猩红"),
}

# 全局工作模式: 'low_sat' (默认合规低饱和) | 'original' (原始提取对照)
_CURRENT_MODE = "low_sat"

def set_mode(mode: str) -> None:
    """切换全局调色板工作模式 ('low_sat' 或 'original')"""
    global _CURRENT_MODE
    if mode not in ("low_sat", "original"):
        raise ValueError("模式必须为 'low_sat' 或 'original'")
    _CURRENT_MODE = mode

def get_mode() -> str:
    """获取当前全局调色板工作模式"""
    return _CURRENT_MODE


# =============================================================================
# 2. 点语法安全只读色彩对象 (IDE 自动补全)
# =============================================================================

class _ImmutableColorContainer:
    """只读色彩容器，防止运行时篡改色标"""
    def __init__(self, mode: str = "low_sat"):
        self._mode = mode
        
    def __getattr__(self, name: str) -> str:
        if name in _COLOR_DEFINITIONS:
            # 索引 1 为 low_sat，索引 2 为 original
            idx = 1 if _CURRENT_MODE == "low_sat" else 2
            return _COLOR_DEFINITIONS[name][idx]
        raise AttributeError(f"标准色彩库中不存在色彩名称: '{name}'")
        
    def __setattr__(self, key: str, value: Any) -> None:
        if key in ("_mode",):
            super().__setattr__(key, value)
        else:
            raise PermissionError("标准色彩库为受控只读资产，严禁在运行时修改或添加色卡！")

    def __getitem__(self, name: str) -> str:
        return self.__getattr__(name)

    def get(self, name: str, default: str = "#5A626A") -> str:
        try:
            return self.__getattr__(name)
        except AttributeError:
            return default

    def all_names(self) -> List[str]:
        return list(_COLOR_DEFINITIONS.keys())


# 导出点语法单例
Colors = _ImmutableColorContainer()
C = Colors  # 极简速记别名


# =============================================================================
# 3. 经典调和搭配矩阵 (Harmonies)
# =============================================================================

class _HarmoniesContainer:
    """6 大经典色彩搭配矩阵"""

    @property
    def COMPLEMENTARY(self) -> Tuple[str, str, str]:
        """补色冷暖并置 (冷相基底, 暖相调和, 高辨识警示)"""
        return (C.STEEL_BLUE, C.WARM_AMBER, C.MUTED_CRIMSON)

    @property
    def TETRADIC(self) -> Tuple[str, str, str, str]:
        """四相正交分流 (主向极性 A, 反向极性 B, 侧向分量 L, 侧向分量 R)"""
        return (C.CELADON_MINT, C.DEEP_MOSS, C.SAND_GOLD, C.MUSTARD_OCHRE)

    @property
    def DUAL_CHANNEL(self) -> Tuple[str, str, str, str]:
        """双相平衡对标 (主通道 01, 副通道 02, 辅助流 01, 辅助流 02)"""
        return (C.JADE_GREEN, C.DARK_CYAN, C.AMBER_ORANGE, C.APPLE_GREEN)

    @property
    def ENVELOPE_5(self) -> Tuple[str, str, str, str, str]:
        """五阶色相包线 (下限边界, 过渡阈值, 目标区间, 核心基准, 上限极限)"""
        return (C.MUTED_CRIMSON, C.WARM_AMBER, C.PALE_AQUA, C.STEEL_BLUE, C.ROSE_MAUVE)

    @property
    def GRADIENT_3(self) -> Tuple[str, str, str]:
        """三阶动态阶度 (低幅基底, 常态稳态, 峰值高阶)"""
        return (C.CADET_BLUE, C.TOPAZ_GOLD, C.BRICK_RED)

    @property
    def NEUTRAL_TIER_5(self) -> Tuple[str, str, str, str, str]:
        """明度阶梯分布 (一阶监控, 二阶关注, 三阶跟踪, 四阶保持, 五阶基准)"""
        return (C.PALE_SEAFOAM, C.TURQUOISE_BLUE, C.PETROL_CYAN, C.MIDNIGHT_NAVY, C.SLATE_CHARCOAL)


Harmonies = _HarmoniesContainer()


# =============================================================================
# 4. 场景语义角色映射 (Roles)
# =============================================================================

class _PolarityRoles:
    POSITIVE = C.CELADON_MINT
    NEGATIVE = C.DEEP_MOSS
    LATERAL_L = C.SAND_GOLD
    LATERAL_R = C.MUSTARD_OCHRE

class _DualChannelRoles:
    PRIMARY = C.JADE_GREEN
    SECONDARY = C.DARK_CYAN
    AUX_PRIMARY = C.AMBER_ORANGE
    AUX_SECONDARY = C.APPLE_GREEN

class _TierRoles:
    LEVEL_1 = C.PALE_SEAFOAM
    LEVEL_2 = C.TURQUOISE_BLUE
    LEVEL_3 = C.PETROL_CYAN
    LEVEL_4 = C.MIDNIGHT_NAVY
    LEVEL_5 = C.SLATE_CHARCOAL
    ALERT_LOW = C.CADET_BLUE
    ALERT_MID = C.TOPAZ_GOLD
    ALERT_HIGH = C.BRICK_RED

class Roles:
    """面向数据分析场景的语义角色集合"""
    Polarity = _PolarityRoles
    DualChannel = _DualChannelRoles
    Tiers = _TierRoles


# =============================================================================
# 5. Matplotlib 绘图样式无感注入
# =============================================================================

def apply_style(mode: str = None) -> None:
    """
    一键将 Matplotlib 全局样式配置注入为民航工业克制标准。
    - 设置默认色彩循环 (Color Cycler) 为已审核调和色谱；
    - 配置背景底衬、冷灰网格线与字型设置。
    """
    import matplotlib as mpl
    from cycler import cycler

    if mode:
        set_mode(mode)

    # 经典工业循环色序 (冷蓝 -> 暖琥珀 -> 翡翠青 -> 砖红 -> 灰紫 -> 沙金)
    standard_cycler = cycler(color=[
        C.STEEL_BLUE,
        C.WARM_AMBER,
        C.JADE_GREEN,
        C.BRICK_RED,
        C.PLUM_SLATE,
        C.SAND_GOLD,
        C.TURQUOISE_BLUE,
        C.CORAL_TERRA
    ])

    mpl.rcParams['axes.prop_cycle'] = standard_cycler
    mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Segoe UI', 'DejaVu Sans']
    mpl.rcParams['axes.unicode_minus'] = False
    mpl.rcParams['grid.color'] = '#334155'
    mpl.rcParams['grid.linestyle'] = '--'
    mpl.rcParams['grid.alpha'] = 0.5
    mpl.rcParams['axes.edgecolor'] = '#475569'
    mpl.rcParams['axes.labelcolor'] = '#E2E8F0'
    mpl.rcParams['xtick.color'] = '#94A3B8'
    mpl.rcParams['ytick.color'] = '#94A3B8'


# =============================================================================
# 6. 跨平台资产导出函数 (JSON / CSS)
# =============================================================================

def export_json(filepath: str) -> None:
    """导出色彩库定义为标准 JSON 格式文件"""
    data = {
        "version": VERSION,
        "mode": _CURRENT_MODE,
        "total_colors": len(_COLOR_DEFINITIONS),
        "colors": {
            k: {
                "name": v[0],
                "low_sat": v[1],
                "original": v[2],
                "family": v[3],
                "description": v[4]
            }
            for k, v in _COLOR_DEFINITIONS.items()
        }
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def export_css(filepath: str) -> None:
    """导出色彩库定义为 CSS 根变量文件"""
    lines = [
        "/* 标准色彩库 CSS 变量定义 (版本: " + VERSION + ") */",
        ":root {"
    ]
    for k, v in _COLOR_DEFINITIONS.items():
        css_var_name = "--color-" + k.lower().replace("_", "-")
        lines.append(f"  {css_var_name}: {v[1]}; /* 原版: {v[2]}, {v[4]} */")
    lines.append("}")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
