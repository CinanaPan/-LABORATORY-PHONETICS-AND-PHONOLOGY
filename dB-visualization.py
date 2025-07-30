import matplotlib.pyplot as plt
import numpy as np

# 数据准备 (使用均值数据)
conditions = {
    "Broad Focus": [65.4, 62.8, 61.3],
    "Narrow-Mel": [67.4, 57.4, 57.3],
    "Narrow-wear": [63.7, 63.2, 57.0],
    "Narrow-lily": [66.6, 64.7, 63.0]
}

# 创建坐标标签
positions = ["Melanie's", "wearing a", 
            "lily"]

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
plt.title("Intensity Patterns Across Focus Conditions\n[Athlone Irish English]", 
          fontsize=14, pad=20)
plt.xlabel("Syllable Position",fontsize=10, labelpad=10)
plt.ylabel("Peak Intensity(dB)", fontsize=12, labelpad=15)
plt.xticks(x, positions, rotation=45, ha='right', fontsize=11)
plt.yticks(np.arange(55, 75, 5), fontsize=11)
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
