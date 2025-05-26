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
    std::vector<int>::iterator q;
    for(q=vec.begin(); q<vec.end(); q++){
        std::cout << *q << " ";
    }

    // 使用 std::list
    std::list<int> lst = {10, 20, 30};
    lst.push_front(5); // 在 list 前端添加元素
    for (int l : lst) {
        std::cout << l << " "; // 输出: 5 10 20 30
    }
    std::list<int>::iterator p;
    for(p=lst.begin(); p!=lst.end(); p++){
        std::cout << *p << " ";
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

## vector与list

- list（双向链表）: 基于链表实现，存储内存不连续。迭代器为双向迭代器，仅支持双向移动（++ 和 --），不支持`<`等比较
- vector（动态数组）: 元素存储内存连续。迭代器属于随机访问迭代器，支持所有双向迭代器操作外加比较操作等。

**总结**：

| 特性                | `std::list`                  | `std::vector`                |
|---------------------|------------------------------|------------------------------|
| **迭代器类型**       | 双向迭代器                   | 随机访问迭代器               |
| **支持 `<` 比较**    | 否（设计禁用）               | 是（内存连续，高效）         |
| **时间复杂度**       | 不适用                       | O(1)（地址直接比较）         |
| **通用性建议**       | 必须用 `!=` 或 `==`          | 推荐用 `!=`，但允许 `<`       |


## map与tuple

`std::map` 和 `std::tuple` 是 C++ 标准库中两个完全不同的容器/数据结构，它们的用途、设计思想和操作方式有显著区别。以下是它们的核心区别：

---

### **1. 设计目的**
- **`std::map`**  
  - **关联容器**：用于存储键值对（`key-value`），提供基于键的快速查找（时间复杂度为 O(log n)）。  
  - **动态结构**：元素可动态插入、删除，键是唯一的（若需重复键，使用 `std::multimap`）。  
  - **有序性**：默认按键升序排列（基于红黑树实现）。

- **`std::tuple`**  
  - **固定大小的异构容器**：用于将多个不同类型的值组合成一个单一对象，元素的数量和类型在编译时确定。  
  - **静态结构**：创建后不能增删元素，只能访问或修改现有元素。  
  - **无键值概念**：元素通过位置（索引）访问。



### **2. 访问方式**
- **`std::map`**  
  - 通过**键**访问值（类似字典）：  
    ```cpp
    std::map<std::string, int> scores = {{"Alice", 90}, {"Bob", 85}};
    int alice_score = scores["Alice"]; // 90
    ```
  - 支持迭代器遍历（遍历键值对）：  
    ```cpp
    for (const auto& [key, value] : scores) {
        std::cout << key << ": " << value << std::endl;
    }
    ```

- **`std::tuple`**  
  - 通过**索引**（编译时常量）访问元素：  
    ```cpp
    std::tuple<int, std::string, double> data(42, "Hello", 3.14);
    int num = std::get<0>(data);      // 42
    std::string str = std::get<1>(data); // "Hello"
    ```
  - 或通过**结构化绑定**（C++17+）：  
    ```cpp
    auto [num, str, val] = data; // num=42, str="Hello", val=3.14
    ```
  - **无法动态遍历**（元素类型和数量在编译时固定）。



### **5. 性能对比**
| **特性**       | **`std::map`**                | **`std::tuple`**              |
|----------------|-------------------------------|-------------------------------|
| **内存占用**   | 较高（树节点开销）            | 低（紧凑布局）                |
| **查找速度**   | O(log n)（基于键）            | 不支持按内容查找              |
| **插入/删除**  | O(log n)                      | 不支持动态增删                |
| **遍历速度**   | O(n)（顺序遍历）              | 无法动态遍历                  |

---

### **6. 代码示例对比**
#### 使用 `std::map`：
```cpp
#include <map>
#include <string>

int main() {
    std::map<std::string, int> ages;
    ages["Alice"] = 30;
    ages["Bob"] = 25;

    // 查找操作
    if (ages.find("Alice") != ages.end()) {
        std::cout << "Alice's age: " << ages["Alice"] << std::endl;
    }
    return 0;
}
```

#### 使用 `std::tuple`

```cpp
#include <tuple>
#include <iostream>

int main() {
    std::tuple<std::string, int, double> person("Alice", 30, 165.5);
    
    // 访问元素
    std::cout << "Name: " << std::get<0>(person) << std::endl;
    std::cout << "Age: " << std::get<1>(person) << std::endl;

    // 修改元素
    std::get<1>(person) = 31;
    return 0;
}
```

### **总结**

- **`std::map`**：适合需要**动态管理键值对**且需要**按键快速查找**的场景。  
- **`std::tuple`**：适合将**固定数量、不同类型的值**组合成一个轻量级对象，常用于函数多返回值或临时数据包装。  

若需要固定大小的键值对，可以使用 `std::pair`（`std::tuple` 的特例，仅包含两个元素）。


### map问题

当通过 operator[]（方括号）访问一个不存在的键时，std::map 会自动插入该键，并调用值类型的默认构造函数初始化对应的值。
即使你没有显式赋值，这个键值对也会被插入到 map 中。

示例：

```cpp
if(player["winner"] == 1){...}
m[1] = "one";//自动插入键值对
```





