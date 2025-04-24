# 构造函数（Constructor）

构造函数是在创建对象时自动调用的特殊函数，用于初始化对象的状态。它的主要作用是为对象的成员变量赋初值，或执行对象创建时需要的其他操作。
只要类内有构造函数，编译器就不会生成缺省参数的构造函数，否则会生成。如果只定义了非缺省参数的构造函数，那么由于编译器不会生成缺省参数的构造函数，所以在类实例化时必须显式调用非缺省参数的构造函数。

## 特点

- **名称**：构造函数的名称必须与类名相同。
- **没有返回类型**：构造函数没有返回类型，甚至不可以声明 `void` 返回类型。
- **自动调用**：当对象被创建时，构造函数会自动调用。
- **重载**：可以定义多个构造函数，使用不同的参数来实现对象的不同初始化方式。

## 种类

1. **默认构造函数（Default Constructor）**：没有参数，或者所有参数都有默认值。
2. **参数化构造函数（Parameterized Constructor）**：带有参数，用于提供初始化值。
3. **拷贝构造函数（Copy Constructor）**：用于通过另一个对象来创建新对象。

## 示例代码：构造函数

```cpp
#include <iostream>
using namespace std;

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

## private构造函数（单例模式）

- 当构造函数被声明为 `private`时，不可以在类外直接构造类的实例。这可应用于单例模式，确保一个类只有一个实例，并提供一个全局访问点，防止外部代码直接创建该类的多个实例，


```cpp
class Singleton {
private:
    // 私有构造函数，禁止外部创建对象
    Singleton() {}

    // 静态成员变量，保存唯一实例
    static Singleton* instance;

public:
    // 获取唯一实例的静态方法
    static Singleton* getInstance() {
        if (instance == nullptr) {
            instance = new Singleton();
        }
        return instance;
    }

    // 可以添加一些公共方法
    void doSomething() {
        // ...
    }
};

// 静态成员初始化
Singleton* Singleton::instance = nullptr;
Singleton* instance1 = Singleton::getInstance();
instance1->doSomething();

```

外部代码只能通过 getInstance() 静态方法来访问单一实例。

- 既然单例对象的构造函数是私有的，那么它不能被直接拷贝，意味着你不能将单例对象作为函数的参数（按值传递）或返回值（按值返回），因为当类作为参数或返回值时会调用拷贝函数，而拷贝构造函数被调用时会试图创建一个新对象。如果想传参需要使用单例对象的引用或指针。

```cpp
void foo(Singleton s) {// 错误：不能按值传递单例对象
    // ...
}
Singleton createSingleton() {
    return Singleton::getInstance(); // 错误：不能返回一个被拷贝的对象
}

```


## 拷贝构造函数（Copy Constructor）

拷贝构造函数是用于通过已有对象创建新对象的一种构造函数。拷贝构造函数的作用是对对象进行“深拷贝”或者“浅拷贝”。

- 浅拷贝是按值逐个拷贝对象中的成员变量。当类中包含指针成员或动态分配的内存时，浅拷贝只会复制指针的地址，而不会复制指针指向的数据。这意味着原对象和拷贝对象会**共享同一块内存区域**（即指针指向同一个内存地址）。如果一个对象改变了这块内存的内容，另一个对象也会受到影响。

- 深拷贝会创建新的内存空间，确保每个对象都有自己独立的资源。对于包含指针的成员变量，深拷贝会在拷贝过程中分配新的内存空间，并将指针指向的数据复制过来，这样每个对象有独立的内存区域。


### 特点

- **拷贝构造函数的定义**：`ClassName(const ClassName& other)`
- 通常，编译器会提供一个默认的拷贝构造函数，它执行“浅拷贝”（成员变量按值复制）。如果类中包含指向动态分配内存的指针，可能需要自定义拷贝构造函数来避免浅拷贝。


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
   当一个函数返回一个对象时，通常会调用拷贝构造函数来复制返回值。

    ```cpp
   MyClass func() {
       MyClass obj;
       return obj; // 调用拷贝构造函数返回对象
   }
   ```

4. **赋值操作**：
   如果使用拷贝赋值操作符（而不是直接初始化），那么会调用拷贝构造函数。虽然通常使用的是 **赋值运算符**，但在某些情况下（例如对对象进行赋值时），可能需要调用拷贝构造函数。


### 示例代码：拷贝构造函数

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

    // 拷贝构造函数
    MyClass(const MyClass& other) {
        ptr = new int(*(other.ptr));  // 深拷贝
        cout << "Copy constructor called, copied value = " << *ptr << endl;
    }
};

int main() {
    MyClass obj1(10);  // 调用构造函数
    MyClass obj2 = obj1;  // 调用拷贝构造函数

    return 0;
}
```


```v
Constructor called, value = 10
Copy constructor called, copied value = 10
```


- 当 `obj2` 被创建时，编译器调用了 `obj1` 的拷贝构造函数，将 `obj1` 的数据深拷贝给 `obj2`。
- 通过自定义的拷贝构造函数，确保每个对象都有自己的内存副本，避免了浅拷贝可能带来的问题（如双重释放内存）。


**与赋值运算符重载区别**：

```cpp
MyClass obj1(1);
MyClass obj2 = obj1;//声明时初始化：调用拷贝构造函数
MyClass obj3;       //调用默认构造函数
obj3 = obj2;        //已定义对象赋值：调用赋值运算符重载函数
```
