import matplotlib.pyplot as plt
import numpy as np

# 数据准备 (使用均值数据)
conditions = {
    "Broad Focus": [206, 190, 174, 166, 188, 157],
    "Narrow-Mel": [237, 152, 144, 134, 134, 129],
    "Narrow-wear": [191, 170, 192, 136, 136, 129],
    "Narrow-lily": [194, 182, 180, 166, 197, 142]
}

# 创建坐标标签
positions = ["Mel (pt.1)", "Mel (pt.2)", 
            "wear (pt.1)", "wear (pt.2)",
            "lil (pt.1)", "lil (pt.2)"]

x = np.arange(len(positions))  # x轴坐标
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # 学术配色

# 创建画布
plt.figure(figsize=(12, 6), dpi=150)

# 绘制每条线
for idx, (cond, values) in enumerate(conditions.items()):
    plt.plot(x, values, 
             marker='o', 
             linestyle='--',
             color=colors[idx],
             linewidth=2,
             markersize=8,
             label=cond)

# 添加标注和样式
plt.title("Fundamental Frequency (f0) Patterns Across Focus Conditions\n[Athlone Irish English]", 
          fontsize=14, pad=20)
plt.xlabel("Measurement Points (Syllable Position × Time Point)", fontsize=10, labelpad=10)
plt.ylabel("f0 (Hz)", fontsize=12, labelpad=15)
plt.xticks(x, positions, rotation=45, ha='right', fontsize=11)
plt.yticks(np.arange(100, 300, 20), fontsize=11)
plt.grid(True, alpha=0.3, linestyle=':')



# 添加图例
plt.legend(title="Focus Conditions:", 
           bbox_to_anchor=(0.5, -0.5), 
           loc='upper center',
           ncol=4,
           frameon=False,
           fontsize=10,
           title_fontsize=10)

plt.tight_layout()
plt.show()
