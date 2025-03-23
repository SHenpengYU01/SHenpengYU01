# 容器 （Container）

在 C++ 中，**容器（container）** 是一种数据结构，用来存储和管理一组元素。C++ 标准库提供了多种不同类型的容器，每种容器都有自己的特点和适用场景。容器通常分为以下几类：

1. **序列容器（Sequence Containers）**  
   序列容器维护元素的线性顺序，元素之间按一定顺序排列。

   - `std::vector`：动态数组，支持随机访问，元素可以在末尾添加或删除。
   - `std::deque`：双端队列，支持在两端快速添加和删除元素。
   - `std::list`：双向链表，支持在两端快速添加和删除元素，但不支持随机访问。
   - `std::array`：固定大小的数组，大小在编译时已确定，支持随机访问。
   - `std::forward_list`：单向链表，只支持从前端快速添加和删除元素。

2. **关联容器（Associative Containers）**  
   关联容器存储键值对并按一定的顺序（通常是基于键的排序）进行组织。元素之间是通过键关联的。

   - `std::set`：存储唯一元素，元素按顺序排列，不支持重复。
   - `std::map`：存储键值对，键唯一，按键排序，支持查找、插入和删除。
   - `std::multiset`：类似于 `set`，但允许存储重复元素。
   - `std::multimap`：类似于 `map`，但允许键重复。

3. **无序容器（Unordered Containers）**  
   无序容器存储键值对并不保证元素的顺序，而是使用哈希表来组织元素。

   - `std::unordered_set`：存储唯一元素，不保证顺序。
   - `std::unordered_map`：存储键值对，键唯一，不保证顺序。
   - `std::unordered_multiset`：存储元素，允许重复元素，不保证顺序。
   - `std::unordered_multimap`：存储键值对，键允许重复，不保证顺序。

4. **适配器容器（Container Adapters）**  
   适配器容器为其他容器提供不同的接口，它们本质上是对其他容器的封装。

   - `std::stack`：栈，支持 LIFO（后进先出）操作，底层容器通常是 `deque` 或 `vector`。
   - `std::queue`：队列，支持 FIFO（先进先出）操作，底层容器通常是 `deque`。
   - `std::priority_queue`：优先队列，支持按优先级顺序访问元素，底层容器通常是 `vector`。

## 示例代码：使用不同的容器

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <unordered_map>

int main() {
    // 使用 std::vector
    std::vector<int> vec = {1, 2, 3, 4};
    vec.push_back(5); // 向 vector 末尾添加元素
    for (int v : vec) {
        std::cout << v << " "; // 输出: 1 2 3 4 5
    }
    std::cout << std::endl;

    // 使用 std::list
    std::list<int> lst = {10, 20, 30};
    lst.push_front(5); // 在 list 前端添加元素
    for (int l : lst) {
        std::cout << l << " "; // 输出: 5 10 20 30
    }
    std::cout << std::endl;

    // 使用 std::set
    std::set<int> s = {3, 1, 4, 1, 5};
    for (int x : s) {
        std::cout << x << " "; // 输出: 1 3 4 5
    }
    std::cout << std::endl;

    // 使用 std::map
    std::map<int, std::string> m;
    m[1] = "apple";
    m[2] = "banana";
    m[3] = "cherry";
    for (const auto& p : m) {
        std::cout << p.first << ": " << p.second << std::endl; // 输出键值对
    }

    // 使用 std::unordered_map
    std::unordered_map<int, std::string> umap;
    umap[10] = "orange";
    umap[20] = "grape";
    umap[30] = "melon";
    for (const auto& p : umap) {
        std::cout << p.first << ": " << p.second << std::endl; // 输出键值对，顺序不定
    }

    return 0;
}
```

