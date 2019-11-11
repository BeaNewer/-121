# -121
自己写的一点点爬虫，
占位符：
tf.placeholder( dtype,shape=None, name=None)
![890cc6a488c378f289afcc1af942a912.png](en-resource://database/1029:1)
![a6626f53cc97ea57145644d5660b46c7.png](en-resource://database/1031:1)

### 1.创建张量
tf.zeros,ones,fill([行，列]，num)，
##### 用已知常数创建：
tf,constant([1,2,3])
##### 相似常量
![df9894f5de1b99c122a9f67f5d060d4f.png](en-resource://database/1033:1)
### 2.变量
![96a1e6a9b4beec0677a9473115ba3561.png](en-resource://database/1035:1)
     变量是 TensorFlow机器学习算法的参数，TensorFlow维护（调整）这些变量的 状态来优化机器学习算法。
### 3.占位符
占位符是TensorFlow对象，用于表示输入输 出数据的格式，允许传入指定类型和形状的数据，并依赖计算图的计算 结果，比如，期望的计算结果。

![62c562ed23a01e6bd4f14517ef8f5cf5.png](en-resource://database/1037:1)
##### 自我总结流程
张量，变量声明。占位符声明，操作声明，初始化变量，run里面给占位符赋值
