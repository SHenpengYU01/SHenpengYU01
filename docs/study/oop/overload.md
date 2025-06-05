# 重载（overloading）

在 C++ 中，**重载（Overloading）** 允许在同一作用域内定义多个名称相同但参数列表不同的函数或运算符。编译器会根据调用时的上下文（如参数类型、数量、顺序）自动选择最匹配的版本。重载的核心目的是提高代码的灵活性和可读性。

C++ 中主要有两种类型的重载：函数重载和操作符重载。

## **函数重载（Function Overloading）**

- **定义**：在同一作用域内定义多个同名函数，但它们的**参数列表**（参数类型、数量、顺序）必须不同。
- **关键点**：
  - 返回类型不能作为重载依据。
  - 常成员函数与非常成员函数可以构成重载（`const` 修饰的成员函数）。
- **示例**：

```cpp
void print(int x) { /* 处理 int 类型 */ }
void print(double x) { /* 处理 double 类型 */ }
void print(const string& s) { /* 处理字符串 */ }
```

**典型应用**：

- 构造函数重载（通过不同参数初始化对象）。
- 工具函数的多版本支持（如处理不同数据类型的 `max` 函数）。


## 操作符重载（Operator Overloading）

- what：在 C++ 中，操作符重载允许你定义或修改标准操作符（如 `+`、`-`、`*`、`[]` 等）对于用户自定义类型的行为。这使得你能够在自定义的类中使用常见的操作符来进行对象间的运算或操作。
- why：操作符重载使得自定义类的对象能够像内建数据类型一样进行运算，从而增强代码的可读性与简洁性。
例如，想要在表示分数的类中使用 `+` 来表示分数的加法运算，或者想要让两个复数对象通过 `*` 来表示复数的乘法运算。

### 基本语法

```cpp
ReturnType operator<operator_symbol>(Parameters) {
    // 函数体
}
```

- **operator<operator_symbol>**：操作符重载的名称，例如 `operator+`、`operator-` 等
- **Parameters**：操作符所需要的参数，通常是与操作符相对应的类型

定义一个重载运算符就像定义一个函数，只是该函数的名字是 operator@，这里@代表运算符。函数参数表中参数的个数取决于两个因素：

1) 运算符是一元的（一个参数）还是二元的（两个参数）。
2) 运算符被定义为全局函数（对于一元是一个参数，对于二元是两个参数）还是成员函数（对于一元没有参数，对于二元是一个参数 — 对象变为左侧参数）。


### 成员函数实现

操作符重载通过成员函数实现时，操作符的左值必须是当前对象本身，右操作数为参数列表中变量


### 友元函数/全局函数实现

操作符重载通过非成员函数实现时，操作符的左值或右值都通过参数列表决定

```cpp
class MyClass {
public:
    friend MyClass operator+(int lhs, const MyClass& rhs);
};

MyClass operator+(int lhs, const MyClass& rhs) { 
    // 左操作数可以是 int，右操作数是 MyClass
    // 实现...
}
// 使用：42 + obj （合法）
```

### 示例：操作符重载

#### **1. 重载加法运算符 (`+`)**

假设我们有一个表示二维点的类，我们希望能够通过 `+` 操作符来计算两个点的和。

```cpp
class Point {
private:
    int x, y;
public:
    Point(int x_val, int y_val) : x(x_val), y(y_val) {}

    // 重载加法操作符
    Point operator+(const Point& other) {
        return Point(x + other.x, y + other.y);
    }

    void print() const {
        cout << "(" << x << ", " << y << ")" << endl;
    }
};

int main() {
    Point p1(1, 2), p2(3, 4);
    Point p3 = p1 + p2;  // 使用重载的加法操作符
    p3.print();  // 输出: (4, 6)
    return 0;
}
```

在这个例子中，`operator+` 重载了加法操作符，使得两个 `Point` 对象可以通过 `+` 运算符进行相加。

#### **2. 重载输入输出操作符 (`<<` 和 `>>`)**

可以重载输入输出操作符来支持用户**自定义类型与流对象的交互**。通常，`<<` 操作符用于输出，`>>` 操作符用于输入。
它们的左操作数必须是ostream，所以不能定义为成员函数。


```cpp
#include <iostream>
using namespace std;

class Point {
private:
    int x, y;
public:
    Point(int x_val = 0, int y_val = 0) : x(x_val), y(y_val) {}

    // 重载输出操作符
    friend ostream& operator<<(ostream& os, const Point& p) {
        os << "(" << p.x << ", " << p.y << ")";
        return os;
    }

    // 重载输入操作符
    friend istream& operator>>(istream& is, Point& p) {
        is >> p.x >> p.y;
        return is;
    }
};

int main() {
    Point p;
    cout << "Enter coordinates for the point (x y): ";
    cin >> p;  // 使用重载的输入操作符
    cout << "The point is: " << p << endl;  // 使用重载的输出操作符
    return 0;
}
```

### **3. 重载比较运算符 (`==`, `!=`, `<`, `>`)**

你可以重载比较运算符来定义对象之间的比较规则。例如，重载 `==` 操作符来检查两个 `Point` 是否相等。

```cpp
#include <iostream>
using namespace std;

class Point {
private:
    int x, y;
public:
    Point(int x_val = 0, int y_val = 0) : x(x_val), y(y_val) {}

    // 重载相等操作符
    bool operator==(const Point& other) const {
        return (x == other.x && y == other.y);
    }

    void print() const {
        cout << "(" << x << ", " << y << ")" << endl;
    }
};

int main() {
    Point p1(1, 2), p2(1, 2), p3(2, 3);
    if (p1 == p2) {
        cout << "p1 is equal to p2" << endl;  // 输出: p1 is equal to p2
    }
    if (p1 != p3) {
        cout << "p1 is not equal to p3" << endl;  // 输出: p1 is not equal to p3
    }
    return 0;
}
```

### **4. 重载数组下标操作符 (`[]`)**

假设我们有一个表示数组的类，并希望能够通过下标操作符访问元素：

```cpp
#include <iostream>
using namespace std;

class Array {
private:
    int arr[10];
public:
    Array() {
        for (int i = 0; i < 10; ++i) {
            arr[i] = 0;
        }
    }

    // 重载数组下标操作符
    int& operator[](int index) {
        if (index >= 0 && index < 10) {
            return arr[index];
        }
        // 如果索引无效，可以抛出异常或返回一个无效值
        throw out_of_range("Index out of range");
    }
};

int main() {
    Array a;
    a[0] = 10;  // 使用重载的下标操作符
    cout << "a[0] = " << a[0] << endl;  // 输出: a[0] = 10
    return 0;
}
```

### **5. 重载赋值运算符 (`=`)**

当你创建一个类时，如果你没有定义赋值运算符，编译器会自动生成一个默认的赋值运算符，但它只是进行**浅拷贝**，即直接拷贝成员变量。如果类包含指针或动态分配的资源，通常需要自定义赋值运算符以避免浅拷贝的问题。

- 注意需要正确处理自赋值情况。

#### 拷贝赋值运算符

进行资源的深拷贝

```cpp
#include <iostream>
using namespace std;

class MyClass {
private:
    int* ptr;
public:
    MyClass(int val) : ptr(new int(val)) {}

    // 自定义赋值运算符
    MyClass& operator=(const MyClass& other) {
        if (this != &other) {  // 避免自我赋值
            delete ptr;  // 删除旧的资源
            ptr = new int(*other.ptr);  // 分配新资源
        }
        return *this;  // 返回当前对象的引用
    }

    void print() const {
        cout << "Value: " << *ptr << endl;
    }

    ~MyClass() {
        delete ptr;  // 释放资源
    }
};

int main() {
    MyClass obj1(10);
    MyClass obj2(20);
    obj2 = obj1;  // 使用重载的赋值运算符
    obj2.print();  // 输出: Value: 10
    return 0;
}
```

#### 移动赋值运算符

```cpp
StrVec &StrVec::operator=(StrVec &&rhs)noexcept
{
    if(this != &rhs){
        free();     //释放当前对象已有资源
        elements = rhs.elements;
        first_free = rhs.first_free;
        cap = rhs.cap;
        //将rhs置于可析构状态
        rhs.elements = rhs.first_free = rhs.cap = nullptr;
    }
    return *this;
}
```

### **6. 解引用运算符 `operator*`**

#### **重载目的**

- 让自定义类型（如智能指针、迭代器）模拟指针行为。
- 控制对象在解引用或取地址时的逻辑。

#### **示例：自定义智能指针**

```cpp
#include <iostream>

template <typename T>
class SmartPtr {
public:
    // 构造函数
    explicit SmartPtr(T* ptr) : ptr_(ptr) {}
    
    // 析构函数（示例，未实现完整 RAII）
    ~SmartPtr() { delete ptr_; }

    // 重载解引用运算符 *
    T& operator*() const {
        return *ptr_;
    }

    // 重载成员访问运算符 ->
    T* operator->() const {
        return ptr_;
    }

private:
    T* ptr_;
};

int main() {
    SmartPtr<int> ptr(new int(42));
    std::cout << *ptr << std::endl; // 输出 42
    return 0;
}
```

#### **关键点**

- `operator*` 返回对象的引用（`T&`），允许修改值。
- 通常与 `operator->` 配合使用，模拟指针行为。
- explicit 关键字通常用于构造函数（尤其是单参数构造函数），防止构造函数被用作隐式类型转换函数，即表明构造函数必须显示调用。
  - 例：
  
  ```cpp
  class MyClass {
    public:
        explicit MyClass(double x) {  // 显式构造函数
            cout << "MyClass constructed with: " << x << endl;
        }
    };
    MyClass obj = 3.14;  // 错误！不允许隐式转换
  ```


### 7. 重载取地址运算符 `operator&`(不建议)

#### **示例：禁用取地址操作**

```cpp
class NoAddress {
public:
    // 重载取地址运算符 &，返回空指针
    NoAddress* operator&() {
        return nullptr; // 阻止获取真实地址
    }
};

int main() {
    NoAddress obj;
    NoAddress* p = &obj; // p 为 nullptr
    return 0;
}
```

#### **注意事项**

- 重载 `operator&` 需谨慎，可能破坏代码逻辑（如 `std::cout << &obj` 会调用自定义逻辑）。
- 实际开发中极少需要重载此运算符。

### 7. ++运算符重载

1. 前置（prefix）递增 (++obj): 先对对象进行增量操作，然后返回该对象的引用。

2. 后置（postfix）递增 (obj++): 先返回对象的原值，然后再对对象进行增量操作。

```cpp
class MyClass {
private:
    int value;
public:
    MyClass(int v) : value(v) {}

    // 前置递增运算符重载
    MyClass& operator++() {
        ++value;  // 先增值
        return *this;  // 返回修改后的对象的引用
    }
    //后置
    MyClass operator++(int) {
        MyClass temp = *this;  // 保存当前对象的副本
        ++value;  // 执行递增操作
        return temp;  // 返回递增之前的原始对象
    }

    int getValue() const {
        return value;
    }
};

int main() {
    MyClass obj(5);
    ++obj;  // 调用前置递增运算符
    std::cout << obj.getValue() << std::endl;  // 输出 6
}
```

注意二者参数列表和返回值的区别：

- prefix：无参数，返回原来对象的引用
- postfix：有个**形式化的参数int**，返回原对象的副本


### 8. 类型转换运算符（`operator char*` 或 `operator int*`）

#### **示例：将类转换为指针类型**

```cpp
class Buffer {
public:
    Buffer() : data_("Hello") {}

    // 重载类型转换运算符，转换为 char*
    operator char*() {
        return data_;
    }

private:
    char data_[64];
};

int main() {
    Buffer buf;
    char* str = buf; // 隐式调用 operator char*()
    cout << *buf << endl;// 这也会隐式调用 operator char*()把buf转化为char*，如果有operator int*()，也可能会调用
    std::cout << str; // 输出 "Hello"
    return 0;
}

```

### **总结**

| **运算符**       | **重载方式**                     | **用途**                     | **示例**               |
|------------------|----------------------------------|------------------------------|------------------------|
| `operator*`      | 成员函数（一元）                 | 解引用自定义指针类型         | 智能指针、迭代器       |
| `operator&`      | 成员函数（一元）                 | 控制取地址行为（极少使用）   | 禁用取地址             |
| `operator T*()`  | 类型转换运算符（可显式/隐式）    | 将类对象转换为指针类型       | 自定义缓冲区转 `char*` |


- **操作符重载**允许自定义类型的对象能够使用标准操作符（如 `+`, `-`, `*`, `[]`, `==` 等）。
- 重载操作符通常通过类的成员函数或友元函数来实现。
- 操作符重载可以增加代码的可读性，使得代码更直观，例如让复数、分数等自定义类型也能支持加法、减法、输入输出等操作。







