# Class

## 访问权限

**private**: 只可在类内使用，被继承也不能使用
**protected**: 继承的子类可以使用，但是类外不可使用
**public**: 类内外都可使用

类内如果不说明访问权限，默认是`private`的。

私有成员的限制是类级别的，而不是对象级别的，所以类的成员函数可以访问同类任何对象的私有成员或函数。

## 初始化参数列表（initializer list）

在 C++ 中，**初始化列表（Initialization List）** 是构造函数中用于直接初始化类成员变量的一种机制。它在构造函数的参数列表后以冒号（`:`）开头，后跟成员变量的初始化表达式。通过初始化列表，成员变量在对象创建时被直接初始化，而不是先默认初始化再赋值。以下是关于初始化列表的详细说明：

---

### **一、初始化列表的语法**

```cpp
class MyClass {
public:
    // 初始化列表位于构造函数参数列表后，以冒号开头
    MyClass(int a, double b) 
        : member1(a),   // 初始化成员变量 member1
          member2(b),   // 初始化成员变量 member2
          refMember(member1),  // 初始化引用成员
          constMember(42)      // 初始化 const 成员
    { 
        // 构造函数体（可执行其他操作）
    }

private:
    int member1;
    double member2;
    int& refMember;    // 引用成员
    const int constMember; // const 成员
};
```

---

### **二、初始化列表的用途**
#### 1. **初始化 `const` 成员**
- `const` 成员变量必须在声明时初始化，且只能在初始化列表中完成。

   ```cpp
   class ConstExample {
   public:
       ConstExample(int val) : constValue(val) {} // 正确
       // ConstExample(int val) { constValue = val; } // 错误！const 成员不能在构造函数体内赋值
   private:
       const int constValue;
   };
   ```

#### 2. **初始化引用成员**

- 引用成员必须在声明时绑定到某个变量，也只能通过初始化列表完成。

   ```cpp
   class RefExample {
   public:
       RefExample(int& ref) : refMember(ref) {} // 正确
   private:
       int& refMember;
   };
   ```

#### 3. **初始化没有默认构造函数的类成员**

- 如果成员是类类型且没有默认构造函数，必须通过初始化列表显式调用其构造函数。

   ```cpp
   class NoDefault {
   public:
       NoDefault(int x) {} // 没有无参构造函数
   };

   class Container {
   public:
       Container() : member(42) {} // 必须通过初始化列表调用 NoDefault 的构造函数
   private:
       NoDefault member;
   };
   ```

#### 4. **提升效率**
- 对于非基本类型（如类对象），使用初始化列表直接调用拷贝构造函数，比在构造函数体内先默认构造再赋值更高效。

   ```cpp
   class EfficientExample {
   public:
       // 高效：直接调用 std::string 的拷贝构造函数
       EfficientExample(const std::string& s) : str(s) {}

       // 低效：先默认构造空字符串，再赋值
       // EfficientExample(const std::string& s) { str = s; }
   private:
       std::string str;
   };
   ```

---

### **三、初始化列表的注意事项**
#### 1. **初始化顺序**
- 成员变量的初始化顺序由它们在类中的**声明顺序**决定，与初始化列表中的书写顺序无关。
- 如果初始化一个成员时依赖另一个成员的值，需确保声明顺序正确。
- 建议按声明顺序初始化。

   ```cpp
   class OrderExample {
   public:
       // 看似错误，实则正确，x先声明的先初始化
       OrderExample(int a) : y(x), x(a) {}
   private:
       int x;
       int y;
   };
   ```

顺序很重要，这是一个实际的例子：

```cpp
class Vector{
  T *m_pElements;
  int m_nSize;
  int m_nCapacity;
  ...    
};
Vector<T>::Vector(const Vector& r):
    m_nSize(r.m_nSize),
    m_nCapacity(r.m_nCapacity > 0 ? r.m_nCapacity : 0),
    m_pElements(r.m_nCapacity > 0 ? new T[m_nCapacity]: nullptr) //T[r.m_nCapacity]
{
    if(r.m_nCapacity > 0){
        cout << m_nCapacity << endl;
        for(int i=0; i < r.m_nSize; i++){
            this->m_pElements[i] = r.m_pElements[i]; // Copy elements
        }
    }
}
```

这里实现Vector的拷贝构造函数，初始化列表中先定义的 `m_pElements` 却依赖于最后定义的 `m_nCapacity`，这极大概率会导致`new`为`m_pElements`分配的内存大小错误。
所以最好不要让初始化参数列表中的参数初始化相互耦合，即使耦合也要让初始化顺序符合声明顺序。  


#### 2. **默认初始化**
- 未在初始化列表中显式初始化的成员变量：
  - 基本类型（如 `int`、`double`）会执行默认初始化（值不确定）。
  - 类类型会调用默认构造函数。若类没有默认构造函数，**必须**通过初始化列表显式初始化。

---

### **四、继承中的初始化列表**
在派生类构造函数中，初始化列表还可用于调用基类的构造函数：

```cpp
class Base {
public:
    Base(int x) : baseX(x) {}
private:
    int baseX;
};

class Derived : public Base {
public:
    Derived(int a, int b) 
        : Base(a),  // 调用基类构造函数
          derivedY(b) 
    {}
private:
    int derivedY;
};
```

---

### **五、类内成员初始化（C++11 起）**
C++11 允许在类声明中直接为成员变量赋默认值（类内成员初始化）。但初始化列表仍可覆盖这些默认值：

```cpp
class InClassInit {
public:
    InClassInit(int val) : data(val) {} // 覆盖默认值 100
    InClassInit() {} // 使用默认值 data = 100
private:
    int data = 100; // 类内成员初始化
};
```

---

### **六、总结**
- **何时使用初始化列表？**
  - 初始化 `const` 成员、引用成员、没有默认构造函数的类成员。
  - 提升非基本类型成员的初始化效率。
  - 显式调用基类构造函数（继承场景）。

- **优点**：
  - 避免不必要的默认构造和赋值操作。
  - 支持必须直接初始化的成员（如 `const` 和引用）。
  - 代码更简洁高效。

- **常见错误**：
  - 初始化顺序与声明顺序不一致。
  - 在初始化列表中引用未初始化的成员。
  - 忘记初始化必须通过列表初始化的成员。


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


## 静态成员变量与函数

- `static`修饰的变量与函数是属于**类本身**的，可以不实例化类直接使用`Class::`来访问，即使修饰的变量和函数是`private`的。

- 静态成员变量的值需要在类加载时初始化，并且它们在所有对象实例之间共享。必须在类外部定义其值，如果在内部（比如声明时或构造函数中）定义值，当实例化多个对象时就会导致静态成员变量重复定义错误。

- 静态成员函数没有 `this` 指针，因为静态成员函数不依赖于具体的对象，所以静态成员函数也不能访问类内的非静态成员变量（因为它们随具体对象变化）。

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



## 常量对象（const object）

- 为了确保 `const` 对象的状态不会被修改，const 对象只能调用类中声明为 const 的成员函数。
- 但是 `mutable` 修饰的成员变量可以在 const 成员函数中被修改：

```cpp
class MyClass {
public:
    void log() const {
        callCount++;  // 合法：mutable 成员变量允许在 const 函数中修改
    }
private:
    mutable int callCount = 0;
};
```

- 同一成员函数可同时有`const`和`非const`版本，编译器会根据调用对象的 const 性自动选择。


## 类的继承

在 C++ 中，**继承（Inheritance）** 是面向对象编程的核心机制之一，允许子类（派生类）复用和扩展父类（基类）的属性和方法。以下是继承的核心知识点和注意事项：


### **一、继承的基本语法**

#### 1. **继承方式**

- **公有继承（public）**：基类的 `public` 和 `protected` 成员在派生类中保持原有访问权限。
- **保护继承（protected）**：基类的 `public` 和 `protected` 成员在派生类中变为 `protected`。
- **私有继承（private）**：基类的所有成员在派生类中变为 `private`（默认继承方式）。


#### 2. **成员访问权限**

| 基类成员权限       | 公有继承（public） | 保护继承（protected） | 私有继承（private） |
|--------------------|--------------------|----------------------|--------------------|
| `public`           | `public`           | `protected`          | `private`          |
| `protected`        | `protected`        | `protected`          | `private`          |
| `private`          | 不可访问           | 不可访问             | 不可访问           |



### **二、继承的核心知识点**

#### 1. **构造函数与析构函数**

- **构造函数调用顺序**：基类构造函数 → 派生类成员构造函数 → 派生类构造函数。
  - why: 派生类的构造函数可能依赖基类已初始化的状态。
- **析构函数调用顺序**：派生类析构函数 → 派生类成员析构函数 → 基类析构函数。
  - why: 派生类的析构函数可能需要依赖自身的成员对象或基类状态。若先销毁基类，派生类析构函数中访问基类成员会导致未定义行为（如访问已释放的内存）。
例

```cpp
class Base {
public:
    Base() { std::cout << "Base constructed\n"; }
};

class Member {
public:
    Member() { std::cout << "Member constructed\n"; }
};

class Derived : public Base {
    Member m; // 成员对象
public:
    Derived() { std::cout << "Derived constructed\n"; }
};

int main() {
    Derived d;
    //顺序： Base constructed、Member constructed、Derived constructed
}
```


- **显式调用基类构造函数**：

  ```cpp
  class Derived : public Base {
  public:
      Derived(int x) : Base(x) { /* ... */ } // 显式调用基类构造函数
  };
  ```


### **三、注意事项**
#### 1. **避免对象切片（Object Slicing）**
- **问题**：将派生类对象赋值给基类对象时，派生类特有部分被“切掉”。

  ```cpp
  Derived d;
  Base b = d; // 对象切片，丢失 Derived 的额外成员
  ```

- **解决方案**：使用指针或引用。

  ```cpp
  Base* ptr = new Derived(); // 正确，通过指针或引用保留多态性
  ```

#### 2. **虚析构函数**
- **必要性**：若基类指针指向派生类对象，基类析构函数必须为虚函数，否则可能内存泄漏。

  ```cpp
  class Base {
  public:
      virtual ~Base() {} // 虚析构函数
  };
  ```

#### 3. **谨慎使用多重继承**
- **问题**：多重继承可能导致逻辑复杂化和菱形继承问题。
- **最佳实践**：优先使用组合（Composition）而非继承，或使用接口类（纯虚类）。

#### 4. **访问基类隐藏成员**
- 若派生类隐藏了基类的同名函数，可通过作用域运算符 `::` 访问：

  ```cpp
  class Derived : public Base {
  public:
      void func() {
          Base::func(); // 调用基类被隐藏的函数
      }
  };
  ```

---

### **四、继承的设计原则**
1. **Liskov 替换原则（LSP）**  
   派生类必须能完全替代基类，不改变基类的原有行为。

2. **优先使用公有继承**  
   除非需要限制基类成员的访问权限，否则使用 `public` 继承。

3. **避免过度继承**  
   继承应表示“is-a”关系，而非单纯复用代码。

---

### **五、示例：继承与多态**

```cpp
#include <iostream>

// 基类
class Animal {
public:
    virtual void speak() { std::cout << "Animal sound\n"; }
    virtual ~Animal() = default;
};
// 派生类
class Dog : public Animal {
public:
    void speak() override { std::cout << "Woof!\n"; }
};

class Cat : public Animal {
public:
    void speak() override { std::cout << "Meow!\n"; }
};

int main() {
    Animal* animals[] = {new Dog(), new Cat()};
    for (auto* animal : animals) {
        animal->speak(); // 多态调用
        delete animal;
    }
    return 0;
}
```

---

### **总结**
- **继承方式**：控制基类成员在派生类中的访问权限。
- **虚函数与多态**：实现运行时多态，需注意虚析构函数。
- **菱形继承**：通过虚继承解决数据冗余。
- **设计原则**：遵循 LSP，优先组合，谨慎使用多重继承。

合理使用继承能提高代码复用性和扩展性，但需避免滥用导致复杂性和维护成本增加。


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

