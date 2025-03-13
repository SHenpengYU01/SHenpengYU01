# The basic knowledge of C++

## 声明与定义

声明：只是向计算机介绍名字。使用`extern`关键字，但是如果是函数可以不使用，不带函数体的函数名连同参数表或返回值，自动地作为一个
声明。
定义：为名字分配内存，它可以同时是声明。


## 头文件

`#include`的头文件如果用标准头文件或标准库一般用`<>`，而自定义头文件一般用`""`，便于区分。

C++标准库头文件不加`.h`，而C标准库头文件需要加，如果在 C++ 中使用，通常使用 `c` 前缀并去掉 `.h` 后缀，如`#include<cstdio>`


防止头文件多次声明导致的错误：

```cpp
// myheader.h
#ifndef MYHEADER_H   // 使用头文件名作为前缀
#define MYHEADER_H
// 头文件的实际内容
#endif

//C++中也可以在头文件中使用如下简化的预处理指令
#pragma once

```

头文件多次声明的例子：`main.cpp`中include `A.h`和`B.h`，而`B.h`中也include了`A.h`，那么`A.h`就在`main.cpp`中声明了两次。

## 作用域

### 范围分解

使用范围分解符`::`可以指定使用哪个范围（全局、类内、结构体内）的变量和函数。

全局范围`::函数/变量名`：

```cpp
int a;
void f(){}
struct S{
    int a;
    void f(){}
}
void S::f(){
    ::a++; //the gobal a
    ::f(); //the gobal f
}
```

## struct

C++中的结构体和类很像，结构体中如果没有范围限定符，默认为`pubilc`，类中默认为`private`。

结构体中可以定义函数，但是C不行，C的结构体只能包含数据成员。C、C++结构体都可以嵌套。

结构体也可以有构造函数：


```cpp
struct MyStruct {
    int x;
    int y;
    // 构造函数
    MyStruct(int a, int b) : x(a), y(b) {}
    // 成员函数，直接访问成员变量并输出
    void display() {
        cout << "x = " << x << ", y = " << y << endl;
    }
};
int main() {
    MyStruct obj(5, 10);  // 创建结构体对象并调用构造函数
    obj.display();         // 调用结构体的成员函数
}
```

声明为静态的变量和函数可在结构体外使用范围分解运算符`::`来访问。

```cpp
struct MyStruct {
    static int x;  // 静态数据成员
    static void showX() {  // 静态成员函数
        cout << "x = " << x << endl;
    }
};
Mystruct::x=10;
Mystruct::showX();
```

## 缺省参数

缺省参数是在函数声明时就已给定的一个值，如果我们在调用函数时没有指定这一参数的值，编译器就会自动地插上这个值。

注意：

- 只有参数列表的后部参数才可是缺省的，也就是说，我们不可以在一个缺省参数后面又跟一个非缺省的参数。
- 一旦我们开始使用缺省参数，那么这个参数后面的所有参数都必须是缺省的。（这可以从第一条中导出。）
- 默认参数的值可以在函数声明中指定，也可以在函数定义中指定，但不能在声明和定义中都给出默认值。

```cpp
// 函数声明：在声明时为参数指定默认值
void greet(string name = "Guest", int times = 1);
int main()...
// 函数定义：不需要再次指定默认值
void greet(string name/*="Guest"*/, int times/*=1*/) {
    for (int i = 0; i < times; ++i) {
        cout << "Hello, " << name << "!" << endl;
    }
}
```

这和python类似。


## void*

C++允许将任何类型的指针赋给 `void *`（这是 `void*` 的最初的意图，它要求 `void*` 足够大，以存放任何类型的指针），但不允许将`void*` 指针赋给任何其他类型的指针。因为C++是类型严格的。在C中两者都可以。


## 输入输出流

### 插入符与提取符

`<<`插入符。`cout`对象和`cerr`对象有插入符
`>>`提取符。每个数据类型都有重载操作符 “>>”，这些数据类型在一个输入语句里作为“ >>”右边参数使用：

```cpp
int a; cin>>a;
float b; cin>>b;
```

### 操纵算子

`std::endl`：输出换行符并刷新输出流（消除所有存储在内部流缓冲区里的还没有输出的字符）
`std::flush`：强制刷新输出流
`std::`


## new and delete

用于堆上分配和释放内存，与C中`malloc`和`free`相似。

```cpp
int* pt=new int;
int* pt1=new int[10];
delete pt;
delete[] pt1;

MyClass* obj = new MyClass;  // 调用构造函数(constructor)
delete obj;                  // 调用析构函数(destructor)并释放内存
```

## Reference

reference(引用)本质是个变量的别名，引用允许我们通过别名访问变量，而不需要复制其值。`type &ref = variable`。
特点：

- 引用在声明时就必须初始化且之后不能改变引用的对象。
- 引用本质上是一个别名，它和原始对象共享同一内存地址。
- 引用用于函数参数传递时，避免了大对象的复制，并且可以在函数内部修改外部对象的值。

用法：

```cpp
void increment(int &x) {
    x++;  // 通过引用修改外部变量的值
}


int& getMax(int &a, int &b) {
    return (a > b) ? a : b;  // 返回引用
}
int x=10,y=20;
getMax(x,y)=30;  //现在y=30


void printValue(const int &x) {//传递大型对象/结构体时尤其重要，可以避免不必要的复制，同时保护原始数据。
    std::cout << x << std::endl;  // 不能修改 x
}
int x;
printValue(x);
```

**与指针的区别**：

| 特性                   | 引用（Reference）                          | 指针（Pointer）                             |
|------------------------|-----------------------------------------|-------------------------------------------|
| **语法**               | `type &ref = variable;`                  | `type* ptr = &variable;`                   |
| **是否可为空**         | 不可为空（必须引用有效的对象）            | 可以为空（指向 `nullptr`）                  |
| **是否可以修改指向对象** | 不可以修改引用指向的对象                  | 可以通过修改指针来改变它指向的对象        |
| **内存开销**           | 引用没有额外的内存开销，它是一个别名      | 指针有额外的内存开销（存储指针本身的地址）  |
| **使用场景**           | 更常用于函数参数传递、返回引用等          | 更灵活，可以指向不同的对象，但需要管理内存 |
| **常量引用**           | `const type &`                           | `const type*`                              |

限制：

- No pointers to reference: `int& * p;//illegal;`
- No array of references

## const

C++中关键字，用于声明常量或常量表达式，表示数据不可修改。

- 编译时常量：编译时就被确定下来，编译器可以直接替换常量值，不会存储在运行时内存
  - `const int x=1;`
- 运行时常量：运行时才能确定，编译器无法确定值：内存中储存其值
  - `const int x;`

!!! tip "使用方式"
    `const` 可在类型前也可在类型后：`const int x;`和`int const x`相同。前者更为常见。

### constexpr

constexpr 声明的常量要求值在编译时可确定

### pointers and const

```cpp
char* const p='123'; //p is a const pointer
p++;//error
*p='abc'//right

const char* q='abc'; //q* is a const char
*q='1';//error
q++; //right

char const* r = &p;//r is a const char
```

## resolver

```cpp
void Dog::eat(){
  ::eat();//without::, eat would be recursively called
  //::eat means eat() is a global function outside of Dog class
  cout<<"Dog is eating";
}
```

## Container

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

### 示例代码：使用不同的容器

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

## Class

### 访问权限

**private**: 只可在类内使用，被继承也不能使用
**protected**: 继承的子类可以使用，但是类外不可使用
**public**: 类内外都可使用

### 构造函数（Constructor）

构造函数是在创建对象时自动调用的特殊函数，用于初始化对象的状态。它的主要作用是为对象的成员变量赋初值，或执行对象创建时需要的其他操作。

#### 特点

- **名称**：构造函数的名称必须与类名相同。
- **没有返回类型**：构造函数没有返回类型，甚至不可以声明 `void` 返回类型。
- **自动调用**：当对象被创建时，构造函数会自动调用。
- **重载**：可以定义多个构造函数，使用不同的参数来实现对象的不同初始化方式。

#### 种类

1. **默认构造函数（Default Constructor）**：没有参数，或者所有参数都有默认值。
2. **参数化构造函数（Parameterized Constructor）**：带有参数，用于提供初始化值。
3. **拷贝构造函数（Copy Constructor）**：用于通过另一个对象来创建新对象。

#### 示例代码：构造函数

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


### 析构函数（Destructor）

析构函数是在对象生命周期结束时（即对象销毁时）自动调用的特殊成员函数。它的主要作用是进行资源清理，例如释放动态分配的内存，关闭文件句柄等。

#### 析构函数的特点

- **名称**：析构函数的名称是类名加 `~` 符号（例如 `~MyClass()`）。
- **没有返回类型**：与构造函数类似，析构函数没有返回类型。
- **没有参数**：析构函数不能带参数，因此不能重载。
- **自动调用**：当对象生命周期结束时，析构函数会自动调用，通常是对象超出作用域时，或者通过 `delete` 关键字删除时。

#### 示例代码：析构函数

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

#### 解释

1. **构造函数**：当对象 `obj` 被创建时，构造函数分配了动态内存。
2. **析构函数**：当 `obj` 超出作用域（即程序结束时），析构函数自动被调用，释放了动态分配的内存。

### 3. 构造函数与析构函数的关系

- 构造函数在对象创建时被调用，负责初始化对象。
- 析构函数在对象销毁时被调用，负责清理资源。

例如，如果一个类中有动态分配的内存或文件句柄等资源，构造函数会负责分配这些资源，而析构函数则负责释放这些资源。

### 4. 拷贝构造函数（Copy Constructor）

拷贝构造函数是用于通过已有对象创建新对象的一种构造函数。拷贝构造函数的作用是对对象进行“深拷贝”或者“浅拷贝”。

#### 拷贝构造函数的特点

- **拷贝构造函数的定义**：`ClassName(const ClassName& other)`
- 通常，编译器会提供一个默认的拷贝构造函数，它执行“浅拷贝”（成员变量按值复制）。如果类中包含指向动态分配内存的指针，可能需要自定义拷贝构造函数来避免浅拷贝。

#### 示例代码：拷贝构造函数

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

    // 析构函数
    ~MyClass() {
        delete ptr;  // 释放动态分配的内存
        cout << "Destructor called, memory freed" << endl;
    }
};

int main() {
    MyClass obj1(10);  // 调用构造函数
    MyClass obj2 = obj1;  // 调用拷贝构造函数

    return 0;
}
```

#### 输出

```v
Constructor called, value = 10
Copy constructor called, copied value = 10
Destructor called, memory freed
Destructor called, memory freed
```

#### 解释

- 当 `obj2` 被创建时，编译器调用了 `obj1` 的拷贝构造函数，将 `obj1` 的数据深拷贝给 `obj2`。
- 通过自定义的拷贝构造函数，确保每个对象都有自己的内存副本，避免了浅拷贝可能带来的问题（如双重释放内存）。


### static变量与函数

`static`修饰的变量与函数是属于类本身的，可以不实例化类直接使用`Class::`来访问：

```cpp
class Room{
  static int door=1;
  static void openDoor(){cout<<"Door was opened.\n";}
};
cout<<Room::door;
Room::openDoor();
```

### 虚函数（Virtual Function）

1. **虚函数的定义**：通过在基类中声明一个函数为虚函数（使用关键字 `virtual`），派生类可以根据需要重新定义（覆盖）该函数。
2. **多态性**：通过基类指针或引用调用虚函数时，程序会根据实际对象的类型调用相应的函数，而不是基类中的函数，这就是**动态绑定（Dynamic Binding）**。

#### 基本语法

```cpp
class Base {
public:
    virtual void display() {  // 基类的虚函数
        std::cout << "Base class display function" << std::endl;
    }
};

class Derived : public Base {
public:
    void display() override {  // 派生类覆盖虚函数
        std::cout << "Derived class display function" << std::endl;
    }
};
```

**`override` 关键字**：这是一个可选的关键字，表明你打算覆盖基类中的虚函数。它有助于编译器检查你是否正确地覆盖了基类的虚函数（例如，函数签名不匹配时会发出警告）。

#### 虚析构函数
虚析构函数是确保在通过基类指针删除派生类对象时能够正确调用派生类的析构函数。没有虚析构函数时，删除派生类对象时会发生未定义行为。

```cpp
class Base {
public:
    virtual ~Base() {  // 虚析构函数
        std::cout << "Base class destructor" << std::endl;
    }
};

class Derived : public Base {
public:
    ~Derived() {
        std::cout << "Derived class destructor" << std::endl;
    }
};

int main() {
    Base* ptr = new Derived();
    delete ptr;  // 正确调用 Derived 和 Base 的析构函数
    return 0;
}
```

输出：

```v
Derived class destructor
Base class destructor
```



