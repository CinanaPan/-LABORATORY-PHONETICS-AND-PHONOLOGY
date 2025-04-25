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
