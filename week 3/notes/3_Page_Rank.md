## PageRank

- Developed by Google founders to measure the importance of webpages from 
the hyperlink network structure. 
- PageRank assigns a score of importance to each node. Important nodes are 
those with many in-links from important pages. 
- PageRank can be used for any type of network, but it is mainly useful for 
directed networks. 
- A node's PageRank depends on the PageRank of other nodes (Circular definition?). 

### Basic PageRank

n = number of nodes in the network 

k = number of steps 

- I. Assign all nodes a PageRank of 1/n 2. Perform the Basic PageRank Update Rule k times. 
- II. Basic PageRank Update Rule: Each node gives an equal share of its current PageRank to all the nodes it links to. 

The new PageRank of each node is the sum of all the PageRank it received from other nodes. 