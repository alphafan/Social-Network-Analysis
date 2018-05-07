## Interpreting PageRank

Random Walker Solution

随机的从一个节点出发，根据它连接的边，走向下一个节点，经过 k 次 walk 之后，
节点的 PageRank 的值就是我们的 walker 访问节点的概率。

## Problem of PageRank Walker Solution

会卡在一些循环的节点列表里面

解决方案：加上一个随机参数 ( dumping parameter )，来跳出循环
