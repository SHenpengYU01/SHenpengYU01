# 友元函数（Friend Function）


- 在 C++ 中，**友元函数（Friend Function）** 是一个能够访问类的私有成员和保护成员（即通常无法访问的成员）的函数，尽管它并不属于该类的成员函数。友元函数可以是类外部的独立函数、类的成员函数、或另一个类的成员函数。

- 当需要与其他类的私有数据进行交互时，或者当两个类需要紧密合作时，通常使用友元函数来提高封装性和可访问性。

## 如何定义

1. **在类定义中声明友元函数**：
   - 通过在类内部使用 `friend` 关键字来声明某个函数为友元函数。

2. **友元函数没有 `this` 指针**：
   - 友元函数不属于类的成员函数，所以它没有 `this` 指针，也不能直接访问类的成员函数，除非它被声明为友元。

## 示例代码

```cpp
class MyClass {
private:
    int x;
public:
    MyClass(int val) : x(val) {}  // 构造函数

    // 声明友元函数
    friend void printValue(const MyClass& obj);  // 友元函数声明
};

// 友元函数定义
void printValue(const MyClass& obj) {
    // 友元函数可以访问 MyClass 的私有成员
    cout << "The value of x is: " << obj.x << endl;
}

int main() {
    MyClass obj(10);
    printValue(obj);  // 调用友元函数，输出：The value of x is: 10
    return 0;
}
```

## 友元函数的特点

1. **不属于类的成员函数**：尽管是友元函数，它不属于类的成员函数，因此没有 `this` 指针。
2. **可以访问私有和保护成员**：友元函数可以直接访问类的私有成员和保护成员，即使它们在外部，但是需要通过类的对象访问，不能向类内函数一样直接访问。
3. **不继承**：如果一个类的某个成员函数是友元函数，这个友元关系不会被继承给派生类。
4. **友元关系是单向的**：如果类 A 的成员函数是类 B 的友元函数，类 B 并不能访问类 A 的私有成员，除非 A 也声明 B 为友元。

## **多个友元函数示例：**

你可以将多个函数声明为友元函数，包括类外部的函数、成员函数，甚至是其他类的成员函数。

```cpp
#include <iostream>
using namespace std;

class A {
private:
    int valueA;
public:
    A(int val) : valueA(val) {}

    // friend class B;      //整个类 B 的所有成员都拥有对类 A 的访问权限
    friend void B::showValue(A&, a);// 特定函数对类A有访问权限
};

class B {
public:
    void showValue(A& a) {
        // 友元函数可以访问 A 类的私有成员
        cout << "The value of A's private member is: " << a.valueA << endl;
    }
};

int main() {
    A a(5);
    B b;
    b.showValue(a);  // 输出：The value of A's private member is: 5
    return 0;
}
```


