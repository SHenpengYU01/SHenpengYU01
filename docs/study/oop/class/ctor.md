# 构造函数（Constructor）

构造函数是在创建对象时自动调用的特殊函数，用于初始化对象的状态。它的主要作用是为对象的成员变量赋初值，或执行对象创建时需要的其他操作。
只要类内有构造函数，编译器就不会生成缺省参数的构造函数，否则会生成。如果只定义了非缺省参数的构造函数，那么由于编译器不会生成缺省参数的构造函数，所以在类实例化时必须显式调用非缺省参数的构造函数。

## 特点

- **名称**：构造函数的名称必须与类名相同，一般为`public`成员。
- **没有返回类型**：构造函数没有返回类型，甚至不可以声明 `void` 返回类型。
- **自动调用**：当对象被创建时，构造函数会自动调用。
- **重载**：可以定义多个构造函数，使用不同的参数来实现对象的不同初始化方式。

## 种类

1. **默认构造函数（Default Constructor）**：没有参数，或者所有参数都有默认值。
2. **参数化构造函数（Parameterized Constructor）**：带有参数，用于提供初始化值。
3. **拷贝构造函数（Copy Constructor）**：用于通过另一个对象来创建新对象。
4. **移动构造函数（Move Ctor）**：通过资源所有权的转移来创建对象

```cpp title="ctor example"

class MyClass {
private:
    int x;
public:
    // 默认构造函数
    MyClass() {
        x = 0;
        cout << "Default constructor called!" << endl;
    }

    // 参数化构造函数
    MyClass(int val) {
        x = val;
        cout << "Parameterized constructor called!" << endl;
    }

    void display() {
        cout << "x = " << x << endl;
    }
};

int main() {
    MyClass obj1;  // 调用默认构造函数
    MyClass obj2(10);  // 调用参数化构造函数

    obj1.display();  // 输出: x = 0
    obj2.display();  // 输出: x = 10

    return 0;
}
```

输出：

```m
Default constructor called!
Parameterized constructor called!
x = 0
x = 10
```

## 拷贝构造函数（Copy Constructor）

拷贝构造函数是用于通过已有对象创建新对象的一种构造函数。拷贝构造函数的作用是对对象进行“深拷贝”或者“浅拷贝”。

!!! info "浅拷贝与深拷贝"
    - 浅拷贝是按值逐个拷贝对象中的成员变量。当类中包含指针成员或动态分配的内存时，浅拷贝只会复制指针的地址，而不会复制指针指向的数据。这意味着原对象和拷贝对象会**共享同一块内存区域**（即指针指向同一个内存地址）。如果一个对象改变了这块内存的内容，另一个对象也会受到影响。

    - 深拷贝会创建新的内存空间，确保每个对象都有自己独立的资源。对于包含指针的成员变量，深拷贝会在拷贝过程中分配新的内存空间，并将指针指向的数据复制过来，这样每个对象有独立的内存区域。


### 如何定义

- **一般定义**：`ClassName(const ClassName& other)`
- 通常，编译器会提供一个默认的拷贝构造函数，它执行“浅拷贝”。如果类中包含指向动态分配内存的指针，可能需要自定义拷贝构造函数来避免浅拷贝。
- 除对象引用参数外的任何额外参数必须提供默认值。

### 调用场景

1. **通过复制初始化创建对象**：
   当你用一个已有对象来**初始化**一个新对象时，会调用拷贝构造函数。
   ```cpp
   MyClass obj1;        // 默认构造函数
   MyClass obj2 = obj1; // 调用拷贝构造函数
   ```

2. **通过传值方式传递对象**：
   当你将一个对象作为函数的参数并且以传值方式传递时，会调用拷贝构造函数。
   ```cpp
   void func(MyClass obj); // 参数是按值传递
   MyClass obj1;
   func(obj1); // 传递时调用拷贝构造函数
   ```

3. **通过返回对象时返回值复制**：
   当一个函数返回一个对象时，可能会调用拷贝构造函数来复制返回值。前提是编译器未启用RVO(return value optimise)，和NRVO(named return value optimise)，且没有定义移动构造函数。
    ```cpp
   MyClass func() {
       MyClass obj;
       return obj; // 调用拷贝构造函数返回对象
   }
   ```

### 示例代码：拷贝构造函数

```cpp
class MyClass {
private:
    int* ptr;
public:
    MyClass(int val) {
        ptr = new int(val);  // 动态分配内存
        cout << "Constructor called, value = " << *ptr << endl;
    }

    // 拷贝构造函数
    MyClass(const MyClass& other) {
        ptr = new int(*(other.ptr));  // 深拷贝
        cout << "Copy constructor called, copied value = " << *ptr << endl;
    }
};

int main() {
    MyClass obj1(10);  // 调用构造函数
    MyClass obj2 = obj1;  // 调用拷贝构造函数
}
```


```v
//输出
Constructor called, value = 10
Copy constructor called, copied value = 10
```

- 当 `obj2` 被创建时，编译器调用了 `obj1` 的拷贝构造函数，将 `obj1` 的数据深拷贝给 `obj2`。
- 通过自定义的拷贝构造函数，确保每个对象都有自己的内存副本，避免了浅拷贝可能带来的问题（如双重释放内存）。


??? note "与赋值运算符重载区别"
    ```cpp
    MyClass obj1(1);
    MyClass obj2 = obj1;//声明时初始化：调用拷贝构造函数
    MyClass obj3;       //调用默认构造函数
    obj3 = obj2;        //已定义对象赋值：调用赋值运算符重载函数
    ```

## 移动构造函数

用于高效地"移动"资源（如动态内存）而非复制，特别适合处理临时对象（右值）的场景。

### 声明形式
```cpp
class MyClass {
public:
    // 移动构造函数
    MyClass(MyClass&& other) noexcept;
};
```

### 关键特性

1. **参数类型**：右值引用 (`&&`)
2. **资源转移**：从源对象"窃取"资源而非复制
3. **源对象状态**：移动后源对象应处于有效但不确定的状态
4. **异常安全**：通常标记为 `noexcept`

## 完整示例

```cpp
#include <iostream>
#include <cstring>

class String {
    char* data;
    size_t length;

public:
    // 普通构造函数
    String(const char* str = "") {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        std::cout << "Constructed: " << data << "\n";
    }

    // 移动构造函数
    String(String&& other) noexcept 
        : data(other.data), length(other.length) {
        
        std::cout << "Move Constructed: " << data << "\n";
        
        // 使源对象处于安全状态
        other.data = nullptr;
        other.length = 0;
    }

    // 析构函数
    ~String() {
        if (data) {
            std::cout << "Destructed: " << data << "\n";
            delete[] data;
        } else {
            std::cout << "Destructed: (moved-from object)\n";
        }
    }

    // 禁用拷贝构造和赋值（仅用于演示）
    String(const String&) = delete;
    String& operator=(const String&) = delete;

    const char* c_str() const { return data; }
};

// 创建临时String的函数
String createString(const char* str) {
    return String(str);
}

int main() {
    // 场景1：从函数返回临时对象
    String s1 = createString("Hello");
    std::cout << "s1: " << s1.c_str() << "\n\n";

    // 场景2：使用std::move显式移动
    String s2 = std::move(s1);
    std::cout << "s2: " << s2.c_str() << "\n";
    std::cout << "s1: " << (s1.c_str() ? s1.c_str() : "nullptr") << "\n\n";

    // 场景3：容器操作中的移动
    std::vector<String> strings;
    strings.push_back(createString("World"));
    std::cout << "Vector element: " << strings[0].c_str() << "\n";

    return 0;
}
```

## 输出示例
```
Constructed: Hello
Move Constructed: Hello
Destructed: (moved-from object)
s1: Hello

Move Constructed: Hello
s2: Hello
s1: nullptr

Constructed: World
Move Constructed: World
Destructed: (moved-from object)
Vector element: World
Destructed: World
Destructed: Hello
Destructed: (moved-from object)
```

### 触发场景

1. **从函数返回临时对象**：
   ```cpp
   String s = createString("Temp");
   ```

2. **使用 `std::move` 显式转换**：
   ```cpp
   String s1("Original");
   String s2 = std::move(s1);
   ```

3. **容器操作**：
   ```cpp
   std::vector<String> vec;
   vec.push_back(String("Element"));
   ```

4. **初始化列表**：
   ```cpp
   String s{String("List")};
   ```

### 实现移动构造函数的最佳实践

1. **资源转移**：直接复制指针而非分配新内存
   ```cpp
   data(other.data)  // 直接转移指针
   ```

2. **置空源对象**：防止源对象析构时释放资源
   ```cpp
   other.data = nullptr;
   ```

3. **标记 noexcept**：允许标准容器优化
   ```cpp
   noexcept
   ```

4. **处理基本类型成员**：直接复制值
   ```cpp
   length(other.length)
   ```

5. **确保源对象可析构**：移动后源对象应处于有效状态

## 编译器生成的移动操作

如果类没有显式声明以下任何成员，编译器会自动生成移动构造函数：
- 拷贝构造函数
- 拷贝赋值运算符
- 移动赋值运算符
- 析构函数

自动生成的移动构造函数会：
1. 对内置类型执行逐成员复制
2. 对类类型成员调用其移动构造函数

### 何时需要自定义移动构造函数

1. 类管理动态内存资源
2. 类包含文件句柄等不可复制资源
3. 需要比编译器默认生成更高效的实现
4. 需要特定的资源转移语义

### 移动语义的优势

1. **性能提升**：避免不必要的深拷贝
2. **资源优化**：减少内存分配/释放操作
3. **支持不可拷贝对象**：如 `std::unique_ptr`
4. **优化返回值**：(N)RVO + 移动语义


编译器通常不会默认生成移动操作的有关函数，比如移动构造函数和移动赋值运算符。

??? info "移动控制"
    1. 只有一个类没有定义任何自己版本的拷贝控制成员，且类的每个非static数据成员都可以移动时，编译器才会为它生成默认的移动构造函数或移动赋值运算符。内置类型成员可移动。  

    2. 定义了一个移动构造函数或移动赋值运算符的类必须定义自己的拷贝操作，否则这些成员默认地被定义为删除的。

    ```cpp
    struct X{
        int i;
        std::string s;
    };  //根据上述1，有默认移动操作
    struct hasX{
        X mem;
    };  //根据1，有默认移动操作
    X x;
    X x2=std::move(x);

    hasX hx;
    haxX hx2 = std::move(hx);
    ```

## 移动构造函数 vs 拷贝构造函数

| 特性         | 移动构造函数               | 拷贝构造函数               |
|--------------|--------------------------|--------------------------|
| **参数类型** | `T&&` (右值引用)         | `const T&` (常量左值引用)|
| **资源操作** | 转移所有权                | 深度复制                 |
| **性能**     | O(1) - 常数时间          | O(n) - 线性时间          |
| **源对象**   | 修改状态（置空指针等）    | 保持不变                 |
| **适用对象** | 临时对象（右值）         | 常规对象（左值）         |


### 移动 or 拷贝？

- 在 C++ 中，从函数返回临时对象时，具体调用的是移动构造函数还是拷贝构造函数，取决于编译器的优化能力和代码的上下文。
- 现代 C++ 编译器（GCC/Clang/MSVC）默认开启优化，返回临时对象**不会调用任何拷贝/移动构造函数**，直接在调用方构造对象。

### 1. **编译器优化优先：返回值优化 (RVO/NRVO)**
现代编译器会优先使用**返回值优化**（Return Value Optimization, RVO）或**命名返回值优化**（Named Return Value Optimization, NRVO），**直接省略拷贝/移动构造**，在调用方直接构造对象。

**示例**：
```cpp
MyClass createObject() {
    return MyClass();  // RVO：直接在调用方构造
}

MyClass createNamed() {
    MyClass obj;       // NRVO：具名对象
    return obj;        // 直接在调用方构造
}

int main() {
    MyClass m1 = createObject();  // 无拷贝/移动
    MyClass m2 = createNamed();   // 无拷贝/移动
}
```

> 在 C++17 后，RVO 成为**强制性优化**（当返回纯右值时）

### 2. **当优化被禁用时：移动优先**
如果编译器无法应用 RVO/NRVO（或使用 `-fno-elide-constructors` 禁用优化），则：
- **优先调用移动构造函数**（如果可用）
- 如果没有移动构造函数，则调用拷贝构造函数

**示例（禁用优化）**：
```cpp
class MyClass {
public:
    MyClass() {}
    MyClass(const MyClass&) { cout << "拷贝构造\n"; }
    MyClass(MyClass&&) { cout << "移动构造\n"; }
};

MyClass create() {
    MyClass obj;
    return obj;  // 禁用优化时
}

int main() {
    MyClass m = create();
}
```

**输出**：
```
移动构造  // 函数内对象移动到函数返回对象
构造函数  // 函数返回对象移动到调用方
```


### 3. **验证实验
```cpp
#include <iostream>
using namespace std;

class Trace {
public:
    Trace() { cout << "默认构造\n"; }
    Trace(const Trace&) { cout << "拷贝构造\n"; }
    Trace(Trace&&) { cout << "移动构造\n"; }
};

Trace createRVO() {
    return Trace();  // 纯右值
}

Trace createNRVO() {
    Trace t;
    return t;       // 具名对象
}

Trace createMove() {
    Trace t;
    return std::move(t);  // 显式移动
}

int main() {
    cout << "--- RVO ---\n";
    Trace t1 = createRVO();
    
    cout << "\n--- NRVO ---\n";
    Trace t2 = createNRVO();
    
    cout << "\n--- std::move ---\n";
    Trace t3 = createMove();
}
```

**可能输出（开启优化）**：
```
--- RVO ---
默认构造

--- NRVO ---
默认构造

--- std::move ---
默认构造
移动构造   // std::move 阻止了 NRVO
```

**可能输出（禁用优化）**：
```
--- RVO ---
默认构造
移动构造   // 返回临时对象
移动构造   // 返回局部对象

--- NRVO ---
默认构造
移动构造   // 返回局部对象
移动构造   // 返回局部对象

--- std::move ---
默认构造
移动构造   // 显式移动
移动构造   // 返回局部对象

```

### 总结

| 场景 | 行为 |
|------|------|
| 开启优化（默认） | RVO/NRVO 直接构造（无拷贝/移动） |
| 禁用优化 + 有移动构造 | 调用移动构造函数 |
| 禁用优化 + 无移动构造 | 调用拷贝构造函数 |
| 显式使用 `std::move` | 强制移动（但可能阻止优化） |



