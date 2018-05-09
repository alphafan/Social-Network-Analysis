## Hubs and Authorities 
Given a query to a search engine: 
- __Root:__ set of highly relevant web pages (e.g. pages that contain the query string) - Potential authorities. 
- Find all pages that link to a page in root - potential hubs. 
- __Base:__ root nodes and any node that links to a node in root. 
- Consider all edges connecting nodes in the base set. 

与 PageRank 的区别是，首先只关注某一部分的网络，然后一点一点的扩展开

- 所谓“Authority”页面，是指与某个领域或者某个话题相关的高质量网页，比如搜索引擎领域，
Google和百度首页即该领域的高质量网页，比如视频领域，优酷和土豆首页即该领域的高质量网页。

- 所谓“Hub”页面，指的是包含了很多指向高质量“Authority”页面链接的网页，
比如hao123首页可以认为是一个典型的高质量“Hub”网页。

## HITS Algorithm

HITS算法的目的即是通过一定的技术手段，在海量网页中找到与用户查询主题相关的高质量“Authority”页面和“Hub”页面，尤其是“Authority”页面，
因为这些页面代表了能够满足用户查询的高质量内容，搜索引擎以此作为搜索结果返回给用户。

算法基本思想：相互增强关系
- 基本假设1：一个好的“Authority”页面会被很多好的“Hub”页面指向；
- 基本假设2：一个好的“Hub”页面会指向很多好的“Authority”页面；

## HITS算法存在的问题
        
HITS算法整体而言是个效果很好的算法，目前不仅应用在搜索引擎领域，而且被“自然语言处理”
以及“社交分析”等很多其它计算机领域借鉴使用，并取得了很好的应用效果。尽管如此，
最初版本的HITS算法仍然存在一些问题，而后续很多基于HITS算法的链接分析方法，
也是立足于改进HITS算法存在的这些问题而提出的。

归纳起来，HITS算法主要在以下几个方面存在不足：

1.计算效率较低

因为HITS算法是与查询相关的算法，所以必须在接收到用户查询后实时进行计算，
而HITS算法本身需要进行很多轮迭代计算才能获得最终结果，这导致其计算效率较低，
这是实际应用时必须慎重考虑的问题。

2.主题漂移问题

如果在扩展网页集合里包含部分与查询主题无关的页面，而且这些页面之间有较多的相互链接指向，
那么使用HITS算法很可能会给予这些无关网页很高的排名，导致搜索结果发生主题漂移，
这种现象被称为“紧密链接社区现象”（Tightly-Knit CommunityEffect）。

3.易被作弊者操纵结果

HITS从机制上很容易被作弊者操纵，比如作弊者可以建立一个网页，页面内容增加很多指向高质量网页
或者著名网站的网址，这就是一个很好的Hub页面，之后作弊者再将这个网页链接指向作弊网页，
于是可以提升作弊网页的Authority得分。

4.结构不稳定

所谓结构不稳定，就是说在原有的“扩充网页集合”内，如果添加删除个别网页或者改变少数链接关系，
则HITS算法的排名结果就会有非常大的改变。