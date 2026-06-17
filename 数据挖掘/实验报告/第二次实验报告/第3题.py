import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def main():
    # 1. 引入鸢尾花数据集
    print("正在加载 Iris 鸢尾花数据集...")
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # 2. 随机按8比2划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"数据总数: {len(X)}")
    print(f"训练集样本数: {len(X_train)}")
    print(f"测试集样本数: {len(X_test)}")
    
    # 3. 进行归一化处理 (使用标准化方法 StandardScaler)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 4. 建立逻辑回归模型并使用训练集训练
    model = LogisticRegression(random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # 5. 使用测试集进行测试
    y_pred = model.predict(X_test_scaled)
    
    # 6. 打印准确率
    accuracy = accuracy_score(y_test, y_pred)
    print(f"测试集的预测准确率 (Accuracy): {accuracy * 100:.2f}%")

if __name__ == '__main__':
    main()
