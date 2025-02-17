# Data structure

## Graph

!!! Overall *Introduction*: The graph is powerful tool to handle many practical problems, especially the routine management ones, like crossing the river. There are may algorithms, both referred to in the data structure course and discrete mathematics courses. The theory and the relative proofs are indeed important, which verifies the validity of these algorithms. However, as for my current situation, I think the most urgent thing is to know how to implement the in code.  


### DFS and its application

DFS is used to traverse the graph, each vertex only once, and it will give a spanning tree if we record the edges throughout the whole process.

Here is the general code:
The graph here is a UDAG(undirected acyclic) and unweighted.

```C
void DFS(int G[][], int v, int Nv, int visited[] ){
    visited[v]=1;
    for(int i=0; i<Nv; i++){
        if( G[v][i]&&!visited[i] ){
            DFS(G, i, Nv, visited);
        }
    }
}
```

#### Topological Sort
The graph is a DAG, unweighted and connected.

```C
int top=0;
void DFS(int a[][], int v, int Nv, int visited[], int stack){
    visited[v]=true;
    for(int i=0;i<Nv;i++){
        if(a[v][i]&&!visited[i]){
            DFS(a, i, Nv, visited);
        }
    }
    stack[top++]=v;
}
void topologcial_sort(int G[][], int Nv){
    int stack[Nv];
    int visited[Nv];
    for(int i=0;i<Nv;i++){
        visited[i]=0;
    }
    DFS(G, 0, Nv, visited, stack);
    while(top>-1){
        printf("%d ",stack[top--]);
    }
}
```

#### Circle detection

#### Strongly Connected components computation

Tarjan算法是用来在有向图中寻找强连通分量（Strongly Connected Components, SCC）的经典算法。强连通分量是指一个有向图中的一个最大子图，其中每一对顶点都可以互相到达。Tarjan算法是基于深度优先搜索（DFS）的，并且可以在线性时间内完成（O(V + E)）。

##### Tarjan算法的主要思想

Tarjan算法使用一个栈和一些辅助数组来记录顶点的访问状态。在DFS的过程中，每个顶点都被分配了一个唯一的编号（DFS编号）和一个最低可达编号（Low-link值）。通过这些编号，可以判断顶点是否属于同一个强连通分量。

##### 算法步骤

1. **初始化**：设置DFS编号、Low-link值等辅助数组，并初始化栈。
2. **DFS遍历**：对每个未访问的顶点执行DFS，递归地访问所有可达的顶点。
3. **更新Low-link值**：在DFS过程中更新当前顶点和其后继顶点的Low-link值。
4. **识别强连通分量**：当发现一个顶点的DFS编号和Low-link值相等时，它是一个强连通分量的根节点，将栈中所有到达该顶点的顶点弹出，形成一个强连通分量。

##### 伪代码

下面是Tarjan算法的伪代码：

```pseudo
// n 是图中的顶点数
index = 0
stack = []
indices = [-1] * n
lowlink = [0] * n
onStack = [False] * n
SCCs = []

function strongconnect(v):
    indices[v] = index
    lowlink[v] = index
    index += 1
    stack.push(v)
    onStack[v] = True

    // 考虑 v 的每个后继顶点 w
    for each (v, w) in edges:
        if indices[w] == -1:
            // w 还未访问过，递归访问它
            strongconnect(w)
            lowlink[v] = min(lowlink[v], lowlink[w])
        else if onStack[w]:
            // w 在栈中，是一个回边
            lowlink[v] = min(lowlink[v], indices[w])

    // 如果 v 是一个强连通分量的根节点
    if lowlink[v] == indices[v]:
        SCC = []
        while True:
            w = stack.pop()
            onStack[w] = False
            SCC.append(w)
            if w == v:
                break
        SCCs.append(SCC)

for each v in vertices:
    if indices[v] == -1:
        strongconnect(v)

return SCCs
```

##### C语言实现

下面是Tarjan算法在C语言中的实现：

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 100

int index = 0, n;
int indices[MAX], lowlink[MAX];
bool onStack[MAX];
int stack[MAX], stackTop = -1;
int graph[MAX][MAX];
int SCC[MAX][MAX], SCCIndex = 0, SCCSizes[MAX];

void push(int v) {
    stack[++stackTop] = v;
    onStack[v] = true;
}

int pop() {
    int v = stack[stackTop--];
    onStack[v] = false;
    return v;
}

void strongconnect(int v) {
    indices[v] = lowlink[v] = index++;
    push(v);

    for (int w = 0; w < n; w++) {
        if (graph[v][w]) {
            if (indices[w] == -1) {
                strongconnect(w);
                lowlink[v] = lowlink[v] < lowlink[w] ? lowlink[v] : lowlink[w];
            } else if (onStack[w]) {
                lowlink[v] = lowlink[v] < indices[w] ? lowlink[v] : indices[w];
            }
        }
    }

    if (lowlink[v] == indices[v]) {
        int w;
        do {
            w = pop();
            SCC[SCCIndex][SCCSizes[SCCIndex]++] = w;
        } while (w != v);
        SCCIndex++;
    }
}

void tarjan() {
    for (int i = 0; i < n; i++) {
        indices[i] = -1;
        lowlink[i] = 0;
        onStack[i] = false;
    }

    for (int i = 0; i < n; i++) {
        if (indices[i] == -1) {
            strongconnect(i);
        }
    }
}

int main() {
    printf("Enter the number of vertices: ");
    scanf("%d", &n);

    printf("Enter the adjacency matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &graph[i][j]);
        }
    }

    tarjan();

    printf("Strongly Connected Components:\n");
    for (int i = 0; i < SCCIndex; i++) {
        printf("SCC %d: ", i + 1);
        for (int j = 0; j < SCCSizes[i]; j++) {
            printf("%d ", SCC[i][j]);
        }
        printf("\n");
    }

    return 0;
}
```

##### 解释

1. **初始化**：设置DFS编号数组`indices`和Low-link值数组`lowlink`，初始化栈和相关标记。
2. **递归函数 `strongconnect`**：执行DFS，更新Low-link值，并在发现强连通分量时，将栈中相关顶点弹出，形成强连通分量。
3. **主函数 `tarjan`**：对每个未访问的顶点调用递归函数`strongconnect`。
4. **输入输出**：在`main`函数中读取顶点数量和邻接矩阵，调用`tarjan`算法，输出找到的强连通分量。


Kosaraju-Sharir算法是一种用于在有向图中寻找强连通分量（Strongly Connected Components, SCC）的经典算法。该算法基于两次深度优先搜索（DFS），其时间复杂度为O(V + E)，其中V是顶点数，E是边数。

##### Kosaraju-Sharir算法步骤

1. **反转图**：首先反转图中的所有边，得到一个新的图。
2. **第一次DFS**：对原图进行深度优先搜索，记录每个顶点的完成时间。
3. **第二次DFS**：按照第一次DFS的完成时间的逆序对反转图进行深度优先搜索，找到所有的强连通分量。

##### 算法伪代码

```pseudo
function kosarajuSharir(G):
    let G_rev be the reverse of graph G
    let S be an empty stack
    let visited be a map from node to boolean

    // First DFS: Record the finish time of each node
    function dfs1(v):
        visited[v] = true
        for each neighbor w of v in G:
            if not visited[w]:
                dfs1(w)
        S.push(v)

    // Second DFS: Collect nodes in the same SCC
    function dfs2(v, component):
        visited[v] = true
        component.add(v)
        for each neighbor w of v in G_rev:
            if not visited[w]:
                dfs2(w, component)

    // Initialize the visited map and run the first DFS
    for each vertex v in G:
        visited[v] = false
    for each vertex v in G:
        if not visited[v]:
            dfs1(v)

    // Reinitialize the visited map for the second DFS
    for each vertex v in G:
        visited[v] = false

    // Process all nodes in the order defined by the stack S
    let SCCs be an empty list of components
    while S is not empty:
        v = S.pop()
        if not visited[v]:
            let component be an empty list
            dfs2(v, component)
            SCCs.append(component)

    return SCCs
```

##### C语言实现

以下是Kosaraju-Sharir算法的C语言实现：

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 100

int graph[MAX][MAX];
int graph_rev[MAX][MAX];
bool visited[MAX];
int stack[MAX];
int stackTop = -1;
int SCC[MAX][MAX], SCCIndex = 0, SCCSizes[MAX];
int n;

void push(int v) {
    stack[++stackTop] = v;
}

int pop() {
    return stack[stackTop--];
}

void dfs1(int v) {
    visited[v] = true;
    for (int w = 0; w < n; w++) {
        if (graph[v][w] && !visited[w]) {
            dfs1(w);
        }
    }
    push(v);
}

void dfs2(int v) {
    visited[v] = true;
    SCC[SCCIndex][SCCSizes[SCCIndex]++] = v;
    for (int w = 0; w < n; w++) {
        if (graph_rev[v][w] && !visited[w]) {
            dfs2(w);
        }
    }
}

void kosarajuSharir() {
    // Step 1: Run DFS on the original graph to fill the stack
    for (int i = 0; i < n; i++) {
        visited[i] = false;
    }
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs1(i);
        }
    }

    // Step 2: Reverse the graph
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            graph_rev[i][j] = graph[j][i];
        }
    }

    // Step 3: Run DFS on the reversed graph in the order defined by the stack
    for (int i = 0; i < n; i++) {
        visited[i] = false;
    }
    while (stackTop != -1) {
        int v = pop();
        if (!visited[v]) {
            SCCSizes[SCCIndex] = 0;
            dfs2(v);
            SCCIndex++;
        }
    }
}

int main() {
    printf("Enter the number of vertices: ");
    scanf("%d", &n);

    printf("Enter the adjacency matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &graph[i][j]);
        }
    }

    kosarajuSharir();

    printf("Strongly Connected Components:\n");
    for (int i = 0; i < SCCIndex; i++) {
        printf("SCC %d: ", i + 1);
        for (int j = 0; j < SCCSizes[i]; j++) {
            printf("%d ", SCC[i][j]);
        }
        printf("\n");
    }

    return 0;
}
```

##### 解释

1. **初始化和输入**：读取顶点数量和邻接矩阵，初始化相关数组和变量。
2. **第一次DFS**：对原图执行DFS，按照完成时间将顶点压入栈中。
3. **图反转**：生成反转图，将图中的每条边方向反转。
4. **第二次DFS**：按照第一次DFS的完成时间的逆序对反转图执行DFS，找到所有的强连通分量。
5. **输出结果**：输出所有的强连通分量。

