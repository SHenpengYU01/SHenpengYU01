# C++ 基础语法

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

使用范围分解符/作用域解析符 `::` 可以指定使用哪个范围（全局、类内、结构体内）的变量和函数。

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
    ::f(); //the gobal f，没有::则会递归定义
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
静态成员变量和函数是属于整个结构体/类的，而不是结构体/类的某个实例，所以即使结构体/类的静态成员被声明为 `private`，也可以在定义外访问。

```cpp
struct MyStruct {
private:
static bool is_struct;

public:
    static int x;  // 静态数据成员
    static void showX() {  // 静态成员函数
        cout << "x = " << x << endl;
    }
};

Mystruct::is_struct=false;
Mystruct::x=10;
Mystruct::showX();
```

## 缺省参数

缺省参数是在函数声明时就已给定的一个值，如果我们在调用函数时没有指定这一参数的值，编译器就会自动地插上这个值。

注意：

- 只有参数列表的后部参数才可是缺省的，也就是说，我们不可以在一个缺省参数后面又跟一个非缺省的参数。
- 一旦我们开始使用缺省参数，那么这个参数后面的所有参数都必须是缺省的。（这可以从第一条中导出。）
- 默认参数的值可以在函数声明中指定，也可以在函数定义中指定，但**不能在声明和定义中都给出默认值**，否则就会报默认参数重复定义的错误。

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


void printValue(const int &x) {   //传递大型对象/结构体时尤其重要，可以避免不必要的复制，同时保护原始数据。
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


## 字符串

- "" 代表字符串字面量（const char[]）
- '' 代表字符字面量（char）

```cpp
char a = "A"; //错误 "A" 表示字符串，为 char[2]
char* b = 'B';//错误 'B' 是个字符，为char
```


