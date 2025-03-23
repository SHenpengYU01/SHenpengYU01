# Class

## 访问权限

**private**: 只可在类内使用，被继承也不能使用
**protected**: 继承的子类可以使用，但是类外不可使用
**public**: 类内外都可使用

## 构造函数（Constructor）

构造函数是在创建对象时自动调用的特殊函数，用于初始化对象的状态。它的主要作用是为对象的成员变量赋初值，或执行对象创建时需要的其他操作。
只要类内有构造函数，编译器就不会生成缺省参数的构造函数，否则会生成。如果只定义了非缺省参数的构造函数，那么由于编译器不会生成缺省参数的构造函数，所以在类实例化时必须显式调用非缺省参数的构造函数。

### 特点

- **名称**：构造函数的名称必须与类名相同。
- **没有返回类型**：构造函数没有返回类型，甚至不可以声明 `void` 返回类型。
- **自动调用**：当对象被创建时，构造函数会自动调用。
- **重载**：可以定义多个构造函数，使用不同的参数来实现对象的不同初始化方式。

### 种类

1. **默认构造函数（Default Constructor）**：没有参数，或者所有参数都有默认值。
2. **参数化构造函数（Parameterized Constructor）**：带有参数，用于提供初始化值。
3. **拷贝构造函数（Copy Constructor）**：用于通过另一个对象来创建新对象。

### 示例代码：构造函数

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

### private构造函数（单例模式）

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

## 析构函数（Destructor）

析构函数是在对象生命周期结束时（即对象销毁时）自动调用的特殊成员函数。它的主要作用是进行资源清理，例如释放动态分配的内存，关闭文件句柄等。

### 析构函数的特点

- **名称**：析构函数的名称是类名加 `~` 符号（例如 `~MyClass()`）。
- **没有返回类型**：与构造函数类似，析构函数没有返回类型。
- **没有参数**：析构函数不能带参数，因此不能重载。
- **自动调用**：当对象生命周期结束时，析构函数会自动调用，通常是对象超出作用域时，或者通过 `delete` 关键字删除时。

### 示例代码：析构函数

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

### 解释

1. **构造函数**：当对象 `obj` 被创建时，构造函数分配了动态内存。
2. **析构函数**：当 `obj` 超出作用域（即程序结束时），析构函数自动被调用，释放了动态分配的内存。

## 3. 构造函数与析构函数的关系

- 构造函数在对象创建时被调用，负责初始化对象。
- 析构函数在对象销毁时被调用，负责清理资源。

例如，如果一个类中有动态分配的内存或文件句柄等资源，构造函数会负责分配这些资源，而析构函数则负责释放这些资源。

## 4. 拷贝构造函数（Copy Constructor）

拷贝构造函数是用于通过已有对象创建新对象的一种构造函数。拷贝构造函数的作用是对对象进行“深拷贝”或者“浅拷贝”。

- 浅拷贝是按值逐个拷贝对象中的成员变量。当类中包含指针成员或动态分配的内存时，浅拷贝只会复制指针的地址，而不会复制指针指向的数据。这意味着原对象和拷贝对象会共享同一块内存区域（即指向同一个内存地址）。如果一个对象改变了这块内存的内容，另一个对象也会受到影响。

- 深拷贝会创建新的内存空间，确保每个对象都有自己独立的资源。对于包含指针的成员变量，深拷贝会在拷贝过程中分配新的内存空间，并将指针指向的数据复制过来，这样每个对象有独立的内存区域。


### 特点

- **拷贝构造函数的定义**：`ClassName(const ClassName& other)`
- 通常，编译器会提供一个默认的拷贝构造函数，它执行“浅拷贝”（成员变量按值复制）。如果类中包含指向动态分配内存的指针，可能需要自定义拷贝构造函数来避免浅拷贝。


### 调用场景

1. **通过复制初始化创建对象**：
   当你用一个已有对象来初始化一个新对象时，会调用拷贝构造函数。

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


## 静态成员变量与函数

- `static`修饰的变量与函数是属于类本身的，可以不实例化类直接使用`Class::`来访问，即使修饰的变量和函数是`private`的。

- 静态成员变量的值需要在类加载时初始化，并且它们在所有对象实例之间共享。必须在类外部定义其值，如果在内部（比如声明时或构造函数中）定义值，当实例化多个对象时就会导致静态成员变量重复定义错误。

- 静态成员函数没有 `this` 指针，因为静态成员函数不依赖于具体的对象。

```cpp
class Room{
  static int door=1;
  static void openDoor(){cout<<"Door was opened.\n";}
};
cout<<Room::door;
Room::openDoor();
```

## this 指针

this 指针 是一个 隐式参数，它存在于每个**非静态**成员函数的内部。this 指针指向当前对象的地址，即它指向调用该成员函数的实例（对象）。

基本作用：

- 它使得成员函数能够访问当前对象的成员变量和其他成员函数。
- 它帮助成员函数区分不同的对象，即使它们具有相同的类类型。

```cpp
// x 为类的成员变量
 void setValue(int val) {
    this->x = val;  // 通过 this 指针访问当前对象的成员 x
    // x=val;       // 这样也可以，但是上面写法更容易区分成员变量与其他变量
}
```

## 虚函数（Virtual Function）

1. **虚函数的定义**：通过在基类中声明一个函数为虚函数（使用关键字 `virtual`），派生类可以根据需要重新定义（覆盖）该函数。
2. **多态性**：通过基类指针或引用调用虚函数时，程序会根据实际对象的类型调用相应的函数，而不是基类中的函数，这就是**动态绑定（Dynamic Binding）**。

### 基本语法

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

### 虚析构函数
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


