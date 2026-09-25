# 标准色彩库速查手册

版本：1.0.0
受控状态：已冻结（全量 69 色 · 10 大色彩家族 · 6 组调和搭配）

---

### 一、核心调用方式代码示例

`python
import standard_color_palette as palette
C = palette.C

# 1. 基础点语法调用 (带 IDE 自动补全)
ax.plot(x, y, color=C.STEEL_BLUE)

# 2. 场景角色语义调用
ax.plot(t, ch1, color=palette.Roles.DualChannel.PRIMARY)
ax.plot(t, ch2, color=palette.Roles.DualChannel.SECONDARY)

# 3. 经典调和搭配矩阵调用
env_cols = palette.Harmonies.ENVELOPE_5

# 4. 一键注入 Matplotlib 全局工业样式
palette.apply_style()
`

---

### 二、全量 69 色速查清单 (按 10 大色彩家族分类)

| 英文标识名称 | 低饱和度合规色号 (S<=35%) | 原始提取色号对照 | 所属色彩家族 | 色相特征 |
| :--- | :--- | :--- | :--- | :--- |
| SLATE_CHARCOAL | #5A626A | 同合规色 | SLATE & NAVY | 板岩炭灰 |
| PALE_PLATINUM | #B0B5BA | 同合规色 | SLATE & NAVY | 浅白金灰 |
| DEEP_NAVY | #596C8A | #264C8A | SLATE & NAVY | 深海蓝 |
| SLATE_BLUE | #778EA5 | #6485A5 | SLATE & NAVY | 板岩蓝 |
| ICE_AZURE | #E6F0F8 | 同合规色 | SLATE & NAVY | 冰霜浅青 |
| FOG_BLUE | #D0E2EE | 同合规色 | SLATE & NAVY | 雾蓝 |
| KHAKI_BUFF | #CDC293 | #CDBE7B | SLATE & NAVY | 卡其原沙 |
| STEEL_BLUE | #7893B1 | #5B84B1 | STEEL & OCHRE | 钢蓝 |
| DEEP_TEAL | #5B8080 | #4C8080 | STEEL & OCHRE | 深青 |
| CINNAMON_BROWN | #BD987A | #BD7A42 | STEEL & OCHRE | 肉桂褐 |
| PALE_AQUA | #EAF5F2 | 同合规色 | STEEL & OCHRE | 苍水绿 |
| ROSE_MAUVE | #C8879B | #C86684 | STEEL & OCHRE | 玫瑰锦葵 |
| WARM_AMBER | #D9AF8D | #D97F36 | STEEL & OCHRE | 暖琥珀 |
| GOLDEN_OCHRE | #D9B38D | #D98835 | STEEL & OCHRE | 金赭黄 |
| CORAL_TERRA | #D8908C | #D8554E | STEEL & OCHRE | 珊瑚红 |
| MUTED_CRIMSON | #C78181 | #C72828 | STEEL & OCHRE | 沉暗红 |
| SAGE_GREEN | #81A98F | 同合规色 | MINT & SAGE | 鼠尾草绿 |
| CREAM_YELLOW | #F8E7A2 | 同合规色 | MINT & SAGE | 奶油暖黄 |
| DUSTY_ROSE | #E8ABA7 | #E8928D | MINT & SAGE | 灰玫瑰红 |
| OLIVE_DRAB | #999063 | #998A3D | MINT & SAGE | 暗橄榄 |
| SEA_GREEN | #6CA69F | 同合规色 | MINT & SAGE | 海碧绿 |
| PEWTER_GRAY | #95A1A6 | 同合规色 | MINT & SAGE | 白蜡冷灰 |
| PLUM_SLATE | #7C6A89 | 同合规色 | MINT & SAGE | 灰李紫 |
| LAVENDER_MIST | #E8DCE8 | 同合规色 | MINT & SAGE | 薰衣草雾 |
| CELADON_MINT | #82C18E | 同合规色 | CELADON & SAND | 青瓷绿 |
| DEEP_MOSS | #56755E | 同合规色 | CELADON & SAND | 深苔绿 |
| SAND_GOLD | #F1DC9C | #F1CE63 | CELADON & SAND | 沙金黄 |
| MUSTARD_OCHRE | #E0CA91 | #E0B84C | CELADON & SAND | 芥末赭 |
| INDIGO_SLATE | #7594B4 | #417BB4 | CELADON & SAND | 靛蓝灰 |
| COPPER_RUST | #D8A98C | #D86B26 | CELADON & SAND | 红铜锈 |
| BURNT_UMBER | #8E655C | #8E321E | CELADON & SAND | 焦褐赭 |
| JADE_GREEN | #77B89A | #52B889 | JADE & CYAN | 翡翠绿 |
| DARK_CYAN | #4F7B73 | #327B6F | JADE & CYAN | 暗深青 |
| COBALT_SLATE | #7082A4 | #5672A4 | JADE & CYAN | 钴蓝灰 |
| CLOUD_BLUE | #A4B8CE | 同合规色 | JADE & CYAN | 云水蓝 |
| AMBER_ORANGE | #F1C39C | #F19C52 | JADE & CYAN | 琥珀橙 |
| APPLE_GREEN | #A8CD96 | #9ACD82 | JADE & CYAN | 嫩苹果绿 |
| TANGERINE | #F0C29C | #F08428 | JADE & CYAN | 蜜柑橙 |
| ESPRESSO_BROWN | #6E5547 | #6E381A | JADE & CYAN | 浓缩咖啡褐 |
| FOREST_GREEN | #719D74 | #609D64 | FOREST & BERRY | 苍林绿 |
| SUNFLOWER_GOLD | #E5CB94 | #E5B242 | FOREST & BERRY | 向日葵金 |
| CARROT_ORANGE | #E8BB96 | #E88939 | FOREST & BERRY | 胡萝卜橙 |
| SAFFRON_YELLOW | #D9BE8D | #D9A74A | FOREST & BERRY | 藏红花黄 |
| BERRY_MAGENTA | #D68BA6 | #D65A88 | FOREST & BERRY | 浆果洋红 |
| BLUSH_PINK | #F5DDE6 | 同合规色 | FOREST & BERRY | 浅颊粉 |
| HEATHER_PURPLE | #8F6F8E | 同合规色 | FOREST & BERRY | 石楠紫灰 |
| CADET_BLUE | #9BB2C9 | 同合规色 | CADET & BRICK | 军校灰蓝 |
| TOPAZ_GOLD | #EBC698 | #EBA64E | CADET & BRICK | 黄玉金 |
| BRICK_RED | #C0847C | #C04838 | CADET & BRICK | 砖石红 |
| RAW_SIENNA | #DDB992 | #DDA668 | CADET & BRICK | 生赭黄 |
| GARNET_RED | #9E6966 | #9E3832 | CADET & BRICK | 深石榴红 |
| PALE_SEAFOAM | #BDE8D9 | 同合规色 | TEAL & SEAFOAM | 浅海沫青 |
| TURQUOISE_BLUE | #87B7C1 | #6BB3C1 | TEAL & SEAFOAM | 绿松石蓝 |
| PETROL_CYAN | #668F9D | #32829D | TEAL & SEAFOAM | 石油蓝青 |
| MIDNIGHT_NAVY | #4A5F72 | #1E4B72 | TEAL & SEAFOAM | 午夜藏青 |
| WHEAT_GOLD | #D8C792 | #D8BE6E | TEAL & SEAFOAM | 麦穗金 |
| PINE_GREEN | #689A82 | 同合规色 | TEAL & SEAFOAM | 松针绿 |
| BURNT_ORANGE | #E8B496 | #E86A22 | TEAL & SEAFOAM | 焦橙 |
| WILLOW_GREEN | #8FB89A | 同合规色 | WILLOW & TERRA | 柳叶绿 |
| BARLEY_BUFF | #DDC39C | #DDB87E | WILLOW & TERRA | 大麦原沙 |
| SALMON_CORAL | #E5ADA4 | #E59688 | WILLOW & TERRA | 鲑鱼珊瑚 |
| AQUA_SLATE | #89B9B8 | 同合规色 | WILLOW & TERRA | 水碧灰蓝 |
| GLACIER_MIST | #E6F0F8 | 同合规色 | GLACIER & RUBY | 冰川雾青 |
| CERULEAN_BLUE | #8BB6D1 | #64A8D1 | GLACIER & RUBY | 蔚蓝 |
| SHELL_PINK | #FDECEF | 同合规色 | GLACIER & RUBY | 贝壳淡粉 |
| RUBY_CRIMSON | #C8828E | #C83C55 | GLACIER & RUBY | 红宝石深红 |
| EMERALD_TEAL | #6FA39C | #54A399 | GLACIER & RUBY | 祖母绿青 |
| MARIGOLD_AMBER | #D4B789 | #D49B3E | GLACIER & RUBY | 金盏花琥珀 |
| SCARLET_RED | #C47F83 | #C42730 | GLACIER & RUBY | 深猩红 |

---

### 三、经典调和搭配矩阵速查

1. **补色冷暖并置 (COMPLEMENTARY)**：
   - STEEL_BLUE (#7893B1) · 冷相基底
   - WARM_AMBER (#D9AF8D) · 暖相调和
   - MUTED_CRIMSON (#C78181) · 醒目警示

2. **四相正交分流 (TETRADIC)**：
   - CELADON_MINT (#82C18E) · 主向极性 A
   - DEEP_MOSS (#56755E) · 反向极性 B
   - SAND_GOLD (#F1DC9C) · 侧向分量 L
   - MUSTARD_OCHRE (#E0CA91) · 侧向分量 R

3. **双相平衡对标 (DUAL_CHANNEL)**：
   - JADE_GREEN (#77B89A) · 主通道 01
   - DARK_CYAN (#4F7B73) · 副通道 02
   - AMBER_ORANGE (#F1C39C) · 辅助流 01
   - APPLE_GREEN (#A8CD96) · 辅助流 02

4. **五阶色相包线 (ENVELOPE_5)**：
   - MUTED_CRIMSON (#C78181) · 下限边界
   - WARM_AMBER (#D9AF8D) · 过渡阈值
   - PALE_AQUA (#EAF5F2) · 目标区间
   - STEEL_BLUE (#7893B1) · 核心基准
   - ROSE_MAUVE (#C8879B) · 上限极限

5. **三阶动态阶度 (GRADIENT_3)**：
   - CADET_BLUE (#9BB2C9) · 低幅基底
   - TOPAZ_GOLD (#EBC698) · 常态稳态
   - BRICK_RED (#C0847C) · 峰值高阶

6. **明度阶梯分布 (NEUTRAL_TIER_5)**：
   - PALE_SEAFOAM (#BDE8D9) · 一阶监控
   - TURQUOISE_BLUE (#87B7C1) · 二阶关注
   - PETROL_CYAN (#668F9D) · 三阶跟踪
   - MIDNIGHT_NAVY (#4A5F72) · 四阶保持
   - SLATE_CHARCOAL (#5A626A) · 五阶基准