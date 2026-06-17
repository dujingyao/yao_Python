from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score

# （1）加载手写数字数据集
digits = load_digits()
X = digits.data
y = digits.target

# （2）按照 7:3 的比例拆分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# （3）创建并训练 SVM 分类器
# 此处采用 RBF（高斯）核函数
svm_model = SVC(kernel='rbf', random_state=42)
svm_model.fit(X_train, y_train)

# （4）在测试集上预测结果
y_pred = svm_model.predict(X_test)

# （5）计算指标评估结果
# 因为从 0~9 是十分类问题，因此计算精确率和召回率时需要指定 averge 模式，宏平均（'macro'）较为常用
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')

# 输出测评结果
print("分类结果评估：")
print(f"准确率 (Accuracy) : {accuracy:.4f}")
print(f"精确率 (Precision): {precision:.4f}")
print(f"召回率 (Recall)   : {recall:.4f}")