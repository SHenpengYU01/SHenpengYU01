# 引用（Reference）

引用一种是临时、轻量级的资源访问机制，本质是**变量的别名**，引用允许我们通过别名访问变量，而不需要复制其值。
**1. 格式**：`type &ref = variable`。
**2. 特点**：

- 引用在声明时就必须初始化且之后不能改变引用的对象。
- 引用本质上是一个别名，它和原始对象共享同一内存地址。
- 引用用于函数参数传递时，避免了大对象的复制，并且可以在函数内部修改外部对象的值。

**3. 用法**：

```cpp
void increment(int &x) {
    x++;  // 通过引用修改外部变量的值
}
int& getMax(int &a, int &b) {
    return (a > b) ? a : b;  // 返回引用
}
int x=10,y=20;
getMax(x,y)=30;  //现在y=30
void printValue(const int &x) {   //传递大型对象/结构体时尤其重要，可以避免不必要的复制，同时保护原始数据。
    std::cout << x << std::endl;  // 不能修改 x
}
int x;
printValue(x);
```

**4. 与指针的区别**：

| 特性                   | 引用（Reference）                          | 指针（Pointer）                             |
|------------------------|-----------------------------------------|-------------------------------------------|
| **语法**               | `type &ref = variable;`                  | `type* ptr = &variable;`                   |
| **是否可为空**         | 不可为空（必须引用有效的对象）            | 可以为空（指向 `nullptr`）                  |
| **是否可以修改指向对象** | 不可以修改引用指向的对象                  | 可以通过修改指针来改变它指向的对象        |
| **内存开销**           | 引用没有额外的内存开销，它是一个别名      | 指针有额外的内存开销（存储指针本身的地址）  |
| **使用场景**           | 更常用于函数参数传递、返回引用等          | 更灵活，可以指向不同的对象，但需要管理内存 |
| **常量引用**           | `const type &`                           | `const type*`                              |

**5. 注意**：

- No reference to reference
- No pointers to reference: `int& * p;//illegal;`
- No array of references


## 左右值引用

C中，左右值区别简单：左值可以用于赋值语句左侧，右值不行。
C++中：

- 左值：有持久化内存，对象作为一个左值时使用的是它的内存中的位置。
- 右值：临时的不可持久化的对象，对象作为右值时使用的是其值，内存中的内容。要么是字面常量，要么是表达式求值过程中创建的临时对象。

原则：左值可被当做右值使用（使用其内容），反之不可。

`const i=0;`中i是常量左值。

### 左值引用

也就是默认的引用，如`int &`。

### 右值引用

为支持对象的移动（而非拷贝），引入右值引用：只能绑定到右值的引用，也就是绑定到临时的、即将销毁的对象。

形式：`T&&`即在类型后通过`&&`获得对象引用。

例：

```cpp
int i=0;
int& r=i;//正确
int &&rr=i; //错误：不能将右值引用绑定到左值
int &&rr2 = i*3; //正确
```


!!! tip "std::move"
    utility 标准库中的`std::move`函数可以获得绑定到左值上的右值引用，它接受左值，返回右值引用。

右值引用主要用于两种情况：**移动语义** 和 **完美转发**

#### 移动语义

右值引用实现的移动语义使得临时对象的资源（如动态分配的内存）可以从一个对象“转移”到另一个对象，而不是进行拷贝，提升了性能。

具体包括移动构造函数和移动赋值运算符。
注意：在移动操作完成后，原对象的指针应该被置为空，或者使其进入一个有效的、空的状态。这样，原对象的析构函数不会释放已经转移的资源，并且原对象可以安全地被销毁。


```cpp
#include <iostream>
#include <cstring>

class MyClass {
private:
    char* data;

public:
    // 构造函数
    MyClass(const char* str = "") {
        if (str) {
            data = new char[strlen(str) + 1];
            strcpy(data, str);
        } else {
            data = nullptr;
        }
        std::cout << "Constructor: " << data << std::endl;
    }

    // 移动构造函数
    MyClass(MyClass&& other) noexcept : data(other.data) {
        other.data = nullptr; // 置空原对象的指针
        std::cout << "Move Constructor: " << data << std::endl;
    }

    // 移动赋值运算符
    MyClass& operator=(MyClass&& other) noexcept {
        if (this != &other) {  // 防止自赋值
            delete[] data;     // 释放当前对象的资源

            data = other.data; // 转移资源
            other.data = nullptr; // 将原对象的指针置为空

            std::cout << "Move Assignment: " << data << std::endl;
        }
        return *this; // 支持链式赋值
    }

    // 拷贝构造函数（为了演示）
    MyClass(const MyClass& other) {
        if (other.data) {
            data = new char[strlen(other.data) + 1];
            strcpy(data, other.data);
        } else {
            data = nullptr;
        }
        std::cout << "Copy Constructor: " << data << std::endl;
    }

    // 析构函数
    ~MyClass() {
        delete[] data;
        std::cout << "Destructor: " << (data ? data : "nullptr") << std::endl;
    }

    // 显示数据
    void show() const {
        std::cout << "Data: " << (data ? data : "nullptr") << std::endl;
    }
};

int main() {
    MyClass obj1("Hello");
    MyClass obj2("World");

    obj2 = std::move(obj1);  // 移动赋值

    obj1.show(); // 应该显示 nullptr，因为资源已转移
    obj2.show(); // 应该显示 "Hello"

    return 0;
}
```

### **引用折叠（Reference Collapsing）**

**引用折叠**用来处理引用类型之间的 **组合和转换**，特别是在模板和万能引用的上下文中。引用折叠规则在多重引用类型结合时会产生一个简化后的引用类型。

#### 引用折叠规则

C++ 中的引用折叠规则指出，当 **两个引用类型** 结合在一起时，引用会被折叠为一种较为简单的类型。具体规则如下：

1. **`T& &, T& &&, T&& &`** 都折叠为 **`T&`**。
2. **`T&& &&`** 折叠为 **`T&&`**。


### **万能引用（Universal Reference）**

**万能引用**，又叫做 **转发引用**（Forwarding Reference），用来描述既可以绑定 **左值** 也可以绑定 **右值** 的引用类型。
它的主要特点是：在模板中，引用可以通过 **右值引用** 或 **左值引用** 来推导，这取决于传入的参数类型。

万能引用的定义是 **通过模板类型推导出的右值引用**，即类型为 `T&&`，但是又能够接受 **左值** 和 **右值**。
也就是说，`T&&` 在模板中不仅仅代表右值引用，还可以代表 **万能引用**。


#### 万能引用的示例

```cpp
#include <iostream>
#include <utility> // std::forward

template <typename T>
void f(T&& arg) {
    std::cout << "Received value: " << arg << std::endl;
}

int main() {
    int x = 5;
    f(x); // 传递左值
    f(10); // 传递右值
    return 0;
}
```

**分析**：

- 在模板中，`T&&` 是一个万能引用（转发引用），能够接受 `x`（左值）和 `10`（右值）。
- 编译器会根据传递的实际参数类型推导 `T` 的类型。
  - 当传递 `x` 时，`T` 被推导为 `int&`，所以 `T&&` 会变成 `int& &&`，折叠为 `int&`。
  - 当传递右值 `10` 时，`T` 被推导为 `int`，所以 `T&&` 变成 `int&&`。


### **万能引用和引用折叠的结合**

在模板中，`T&&` 类型的参数可以绑定到左值或右值。当参数是左值时，`T&&` 会被折叠为左值引用（`T&`），而当参数是右值时，`T&&` 会保留为右值引用（`T&&`）。这使得我们可以在函数中正确地转发传入的左值和右值。

#### 转发引用的一个常见例子：完美转发

```cpp
#include <iostream>
#include <utility> // for std::forward

template <typename T>
void forwarder(T&& arg) {
    // 完美转发，保持传入参数的值类别（左值/右值）
    someFunction(std::forward<T>(arg)); 
}

void someFunction(int& x) {
    std::cout << "Left value: " << x << std::endl;
}

void someFunction(int&& x) {
    std::cout << "Right value: " << x << std::endl;
}

int main() {
    int a = 5;
    forwarder(a);      // 调用左值版本
    forwarder(10);     // 调用右值版本
    return 0;
}
```

**分析**：

- `std::forward<T>(arg)` 是为了实现 **完美转发**。它根据 `T` 的类型决定传递 `arg` 时是否保持其左值或右值的性质。
- 如果 `T` 是左值类型（即 `T&`），`std::forward<T>(arg)` 会传递左值引用。
- 如果 `T` 是右值类型（即 `T&&`），`std::forward<T>(arg)` 会传递右值引用。

### 4. **总结：**

- **万能引用** 是指一个模板参数 `T&&`，它可以绑定到左值或右值。它在模板推导中非常有用，可以用于**完美转发**和其他高级用途。
- **引用折叠** 是指两个引用类型结合时会简化为一种类型的规则。引用折叠是 C++ 中模板推导的一部分，确保了引用类型的简化，避免了复杂的类型组合。

通过合理运用 **万能引用** 和 **引用折叠**，我们可以编写更高效、灵活的模板代码，避免不必要的拷贝，减少性能开销。
















