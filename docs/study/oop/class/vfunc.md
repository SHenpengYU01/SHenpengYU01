# 虚函数（Virtual Function）

1. **虚函数的定义**：通过在基类中声明一个函数为虚函数（使用关键字 `virtual`），派生类**可以根据需要**重新定义（覆盖）该函数。
2. **多态性**：通过基类指针或引用调用虚函数时，程序会根据实际对象的类型调用相应的函数，而不是基类中的函数，这就是**动态绑定（Dynamic Binding）**。

## 基本语法

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

## 虚析构函数
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

## 纯虚函数

纯虚函数（pure virtual function）是没有实现的虚函数，它的声明末尾加上 **= 0**。主要作用是强制派生类必须提供该函数的具体实现，否则派生类将变成抽象类，不能实例化。
纯虚函数可以有默认实现：在 C++ 中，纯虚函数仍然可以有一个默认的实现（不常见、不推荐）。虽然派生类必须重写该函数，但如果派生类没有重写，基类的实现将被使用。

## 抽象类

至少含有一个纯虚函数的类是抽象类，不可以直接被实例化。在派生类中必须实现纯虚函数。

```cpp
#include <iostream>
using namespace std;

// 抽象类
class Shape {
public:
    virtual void draw() = 0;
    // 虚析构函数（推荐使用虚析构函数，特别是在继承链中）
    virtual ~Shape() {}
};

class Circle : public Shape {
public:
    void draw() override {
        cout << "Drawing a Circle" << endl;
    }
};

class Rectangle : public Shape {
public:
    void draw() override {
        cout << "Drawing a Rectangle" << endl;
    }
};

int main() {
    // Shape shape;  // 错误：不能实例化抽象类

    // 使用多态创建对象
    Shape* shape1 = new Circle();
    Shape* shape2 = new Rectangle();

    shape1->draw();  // 输出: Drawing a Circle
    shape2->draw();  // 输出: Drawing a Rectangle

    delete shape1;
    delete shape2;

    return 0;
}

```

## 虚函数表

!!! info "动态与静态绑定"
    - 动态绑定（Dynamic Binding）是指在程序运行时（而非编译时）确定具体调用的函数。这可以通过虚表调用虚函数实现。这种行为是运行时多态（Runtime Polymorphism）的体现。
    - 静态绑定：函数调用在编译阶段就可以确定。


在C++中，**虚函数表（vtable）** 是实现动态绑定或运行时多态的底层机制。它的核心思想是通过**间接寻址**，在程序运行时根据对象的实际类型动态确定调用的函数。以下是虚函数表实现动态绑定的详细过程：


### **动态绑定的核心步骤**
1. **虚函数表的创建**  
   - 编译器为**每个包含虚函数的类**生成一个虚函数表（全局唯一）。  
   - 虚表是一个函数指针数组，每个条目对应类的一个虚函数。  
   - **派生类**会继承基类的虚表，并覆盖（Override）基类虚函数的条目，新增的虚函数会追加到虚表末尾。

2. **虚表指针（vptr）的注入**  
   - 每个对象实例的内存布局中，编译器隐式插入一个指针（`vptr`），指向其所属类的虚表。  
   - `vptr`在**对象构造时初始化**，由构造函数负责将其指向正确的虚表。

3. **虚函数调用的寻址**  
   - 当通过基类指针或引用调用虚函数时，编译器生成代码执行以下操作：  
     1. 通过对象的`vptr`找到虚表。  
     2. 根据虚函数在虚表中的**偏移量**（由声明顺序决定）找到函数地址。  
     3. 调用该地址指向的函数。


### **动态绑定过程示例**
#### **1. 类定义**

```cpp
class Animal {
public:
    virtual void speak() { std::cout << "Animal sound" << std::endl; }
    virtual ~Animal() {}
};

class Dog : public Animal {
public:
    void speak() override { std::cout << "Woof!" << std::endl; }
};
```

#### **2. 虚函数表结构**
- **Animal的虚表**：  

  ```a
  [0]: Animal::speak() 的地址  
  [1]: Animal::~Animal() 的地址
  ```

- **Dog的虚表**：  

  ```a
  [0]: Dog::speak() 的地址  // 覆盖基类的speak()  
  [1]: Dog::~Dog() 的地址   // 覆盖基类的析构函数
  ```

#### **3. 对象内存布局**

```cpp
Dog dog; // 对象内存布局示例：
+-------------------+
| vptr → Dog的虚表    |  // 指向Dog的虚表
+-------------------+
| Animal的成员变量    |  // 基类部分
+-------------------+
| Dog的成员变量       |  // 派生类特有部分
+-------------------+
```

#### **4. 动态绑定过程**

```cpp
Animal* animal = new Dog();
animal->speak(); // 运行时动态绑定到Dog::speak()
```

**执行步骤**：  
1. 从`animal`指针找到对象的`vptr`。  
2. 通过`vptr`找到`Dog`的虚表。  
3. 取虚表中第0个条目（`speak()`的地址）。  
4. 调用`Dog::speak()`。


### **动态绑定的关键特性**
#### 1. **运行时决议**
- 函数地址的确定延迟到**运行时**（而非编译时），通过`vptr`和虚表间接寻址。  
- 允许基类指针调用派生类的实现，实现多态。

#### 2. **继承与覆盖**
- 派生类虚表继承基类虚表的结构，覆盖的虚函数会替换对应条目。  
- **多态性**的本质：派生类通过覆盖虚函数，修改虚表内容，改变函数行为。

#### 3. **虚析构函数**
- 若基类析构函数是虚函数，派生类的虚表中会覆盖析构函数条目。  
- 确保通过基类指针删除对象时，调用正确的派生类析构函数。


### **动态绑定的性能与优化**
1. **间接调用开销**  
   - 虚函数调用需要两次内存访问（取`vptr` → 取虚表条目），比普通函数调用稍慢。  
   - 可能影响CPU指令缓存的局部性。

2. **编译器的去虚拟化（Devirtualization）**  
   - 若编译器能在编译期确定对象类型（如`Dog* dog = new Dog()`），可能直接调用`Dog::speak()`，跳过虚表查找。  
   - 常见于简单场景或开启优化（如`-O2`）。


### **动态绑定的本质**
虚函数表的动态绑定机制，本质是**将函数调用从编译期绑定解耦为运行期绑定**。通过`vptr`和虚表，C++实现了以下特性：

- **多态性**：统一接口，多种实现。
- **可扩展性**：新增派生类无需修改基类代码。
- **类型安全**：通过虚表确保函数调用的正确性。


这种机制是C++多态的核心，也是面向对象设计中“一个接口，多种实现”思想的底层支撑。
<img src="\img\study\oop\vtbl.png" alt="vfunc table" title="基类虚拟函数表">

<img src="\img\study\oop\vtbl2.png" alt="vfunc table" title="派生类虚拟函数表">

（上述图源：[博客园](https://www.cnblogs.com/Mered1th/p/10924545.html)）







