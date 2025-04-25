import matplotlib.pyplot as plt
import numpy as np

# 节奏音步数据（均值，单位：ms）
foot_data = {
    "Broad Focus": [511, 340, 314],
    "Narrow-Mel": [492, 305, 275],
    "Narrow-wear": [417, 454, 310],
    "Narrow-lily": [406, 338, 350]
}

syllables = ["Melanie's", "wearing a", "lily"]
x = np.arange(len(syllables))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

plt.figure(figsize=(10, 6), dpi=150)
for idx, (cond, values) in enumerate(foot_data.items()):
    plt.plot(x, values, marker='o', linestyle='--', color=colors[idx], 
             linewidth=2, markersize=8, label=cond)

plt.title("Rhythmic Foot Durations Across Focus Conditions\n[Athlone Irish English]", fontsize=14, pad=20)
plt.xlabel("Rhythmic Foot Position", fontsize=12)
plt.ylabel("Duration (ms)", fontsize=12)
plt.xticks(x, syllables, rotation=15, ha='right', fontsize=11)
plt.yticks(np.arange(250, 600, 50), fontsize=11)
plt.grid(alpha=0.3, linestyle=':')
plt.legend(title="Focus Conditions:", bbox_to_anchor=(0.5, -0.25), loc='upper center', ncol=4, frameon=False)
plt.tight_layout()
plt.show()

# 重音音节数据（均值，单位：ms）
syllable_data = {
    "Broad Focus": [234, 173, 282],
    "Narrow-Mel": [169, 139, 193],
    "Narrow-wear": [184, 265, 207],
    "Narrow-lily": [184, 186, 265]
}

syllables = ["Mel-", "wear-", "lil-"]
x = np.arange(len(syllables))

plt.figure(figsize=(10, 6), dpi=150)
for idx, (cond, values) in enumerate(syllable_data.items()):
    plt.plot(x, values, marker='o', linestyle='--', color=colors[idx], 
             linewidth=2, markersize=8, label=cond)

plt.title("Stressed Syllable Durations Across Focus Conditions\n[Athlone Irish English]", fontsize=14, pad=20)
plt.xlabel("Stressed Syllable", fontsize=12)
plt.ylabel("Duration (ms)", fontsize=12)
plt.xticks(x, syllables, fontsize=11)
plt.yticks(np.arange(100, 350, 50), fontsize=11)
plt.grid(alpha=0.3, linestyle=':')
plt.legend(title="Focus Conditions:", bbox_to_anchor=(0.5, -0.25), loc='upper center', ncol=4, frameon=False)
plt.tight_layout()
plt.show()
