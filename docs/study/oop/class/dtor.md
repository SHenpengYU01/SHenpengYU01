# 析构函数（Destructor）

析构函数是在对象生命周期结束时（即对象销毁时）自动调用的特殊成员函数。它的主要作用是进行资源清理，例如释放动态分配的内存，关闭文件句柄等。

## 析构函数的特点

- **名称**：析构函数的名称是类名加 `~` 符号（例如 `~MyClass()`）。
- **没有返回类型**：与构造函数类似，析构函数没有返回类型。
- **没有参数**：析构函数不能带参数，因此**不能重载**。
- **自动调用**：当对象生命周期结束时，析构函数会自动调用，通常是对象超出作用域时，或者通过 `delete` 关键字删除时。

## 示例代码：析构函数

```cpp
#include <iostream>
using namespace std;

class MyClass {
private:
    int* ptr;
public:
    // 构造函数
    MyClass(int val) {
        ptr = new int(val);  // 动态分配内存
        cout << "Constructor called, value = " << *ptr << endl;
    }

    // 析构函数
    ~MyClass() {
        delete ptr;  // 释放动态分配的内存
        cout << "Destructor called, memory freed" << endl;
    }
};

int main() {
    MyClass obj(5);  // 构造函数被调用，分配内存
    // obj 超出作用域时，析构函数自动调用，释放内存
    return 0;
}
```

输出

```v
Constructor called, value = 5
Destructor called, memory freed
```

## 解释

1. **构造函数**：当对象 `obj` 被创建时，构造函数分配了动态内存。
2. **析构函数**：当 `obj` 超出作用域（即程序结束时），析构函数自动被调用，释放了动态分配的内存。


