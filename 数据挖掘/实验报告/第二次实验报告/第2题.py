import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.datasets import fetch_openml

def main():
    # 1. 引入boston房价数据集
    print("正在下载/加载 Boston 房价数据集...")
    boston = fetch_openml(name='boston', version=1, as_frame=True, parser='auto')
    X = boston.data
    
    # 转换所有列为数值类型
    X = X.apply(pd.to_numeric)
    
    y = boston.target
    
    # 2. 将数据集随机分为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print(f"数据总数: {len(X)}")
    print(f"训练集样本数: {len(X_train)}")
    print(f"测试集样本数: {len(X_test)}")
    
    # 3. 建立多元线性回归模型并使用训练集进行训练
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # 4. 使用测试集进行测试
    y_pred = model.predict(X_test)
    
    # 5. 打印测试集的均方误差 (MSE)
    mse = mean_squared_error(y_test, y_pred)
    print(f"测试集的均方误差 (MSE): {mse:.4f}")

if __name__ == '__main__':
    main()
