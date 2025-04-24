# 类的继承

在 C++ 中，**继承（Inheritance）** 是面向对象编程的核心机制之一，允许子类（派生类）复用和扩展父类（基类）的属性和方法。以下是继承的核心知识点和注意事项：


## **一、继承的基本语法**

### 1. **继承方式**

- **公有继承（public）**：基类的 `public` 和 `protected` 成员在派生类中保持原有访问权限。
- **保护继承（protected）**：基类的 `public` 和 `protected` 成员在派生类中变为 `protected`。
- **私有继承（private）**：基类的所有成员在派生类中变为 `private`（默认继承方式，即没有说明继方式时，默认私有继承）。

子类中不可以直接改变基类成员的访问权限。
当私有继承时，基类的所有 **public成员**都变成了private。如果希望它们中的任何一个是可视的，只要用派生类的public选项声明它们的名字即可

## 2. **成员访问权限**

| 基类成员权限       | 公有继承（public） | 保护继承（protected） | 私有继承（private） |
|--------------------|--------------------|----------------------|--------------------|
| `public`           | `public`           | `protected`          | `private`          |
| `protected`        | `protected`        | `protected`          | `private`          |
| `private`          | 不可访问           | 不可访问             | 不可访问           |



## **二、继承的核心知识点**

### 1. **构造函数与析构函数**

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


## **三、注意事项**
### 1. **避免对象切片（Object Slicing）**
- **问题**：将派生类对象赋值给基类对象时，派生类特有部分被“切掉”。

  ```cpp
  Derived d;
  Base b = d; // 对象切片，丢失 Derived 的额外成员
  ```

- **解决方案**：使用指针或引用。

  ```cpp
  Base* ptr = new Derived(); // 正确，通过指针或引用保留多态性
  ```

### 2. **虚析构函数**
- **必要性**：若基类指针指向派生类对象，基类析构函数必须为虚函数，否则可能内存泄漏。

  ```cpp
  class Base {
  public:
      virtual ~Base() {} // 虚析构函数
  };
  ```

### 3. **谨慎使用多重继承**
- **问题**：多重继承可能导致逻辑复杂化和菱形继承问题。
- **最佳实践**：优先使用组合（Composition）而非继承，或使用接口类（纯虚类）。

### 4. **访问基类隐藏成员**
- 名字隐藏（Name Hiding） 是一种作用域规则现象，当派生类定义了与基类同名的成员（函数或变量）时，基类的**所有同名成员**会被隐藏，导致无法通过派生类直接访问基类成员。
- 若派生类隐藏了基类的同名函数，有如下方法访问基类中隐藏的同名函数：

1. 可通过作用域运算符 `::` 访问：

  ```cpp
  class Derived : public Base {
  public:
      void func() {
          Base::func(); // 调用基类被隐藏的函数
      }
  };
  ```

2. 使用using引入基类成员函数：

```cpp
class Derived : public Base {
public:
    using Base::func; // 引入基类的 func(int)
    void func(double x) { 
        cout << "Derived::func(double)" << endl; 
    }
};

int main() {
    Derived d;
    d.func(42);   // 调用 Base::func(int)
    d.func(3.14); // 调用 Derived::func(double)
    return 0;
}
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

## 非自动继承

在 C++ 中，**并非所有基类函数都能被派生类自动继承**。某些特殊函数需要显式处理，否则会导致功能缺失或未定义行为。以下是需要特别注意的非自动继承函数及其原因：


### **1. 构造函数（Constructors）**
- **规则**：派生类不会自动继承基类的构造函数（包括默认构造、拷贝构造、移动构造等）。
- **原因**：构造派生类对象时，需要确保基类部分和派生类部分都正确初始化。
- **解决方法**：
  - **隐式继承**（C++11+）：使用 `using Base::Base;` 显式继承基类构造函数。
  - **显式定义**：在派生类构造函数中调用基类构造函数。

**示例**：

```cpp
class Base {
public:
    Base(int x) { /*...*/ }
};

class Derived : public Base {
public:
    using Base::Base; // 继承基类构造函数（C++11+）
    // 或显式定义：
    Derived(int x) : Base(x) { /*...*/ }
};
```


### **2. 析构函数（Destructors）**
- **规则**：析构函数不会被继承，但派生类析构函数会自动调用基类析构函数。
- **关键点**：
  - 若基类析构函数是虚函数（推荐），通过基类指针删除派生类对象时，会正确调用派生类析构函数。
  - 若基类析构函数非虚，可能导致资源泄漏（派生类析构函数不执行）。

**示例**：

```cpp
class Base {
public:
    virtual ~Base() { cout << "Base destroyed\n"; } // 虚析构
};

class Derived : public Base {
public:
    ~Derived() { cout << "Derived destroyed\n"; }
};

int main() {
    Base* p = new Derived();
    delete p; // 输出：Derived destroyed → Base destroyed
    return 0;
}
```


### **3. 赋值运算符（Assignment Operators）**
- **规则**：派生类不会自动继承基类的赋值运算符（如 `operator=`）。
- **原因**：派生类需要同时处理自身成员和基类成员的赋值。
- **解决方法**：显式调用基类赋值运算符。

**示例**：

```cpp
class Base {
public:
    Base& operator=(const Base& other) { /*...*/ return *this; }
};

class Derived : public Base {
public:
    Derived& operator=(const Derived& other) {
        Base::operator=(other); // 显式调用基类赋值运算符
        // 处理派生类成员的赋值
        return *this;
    }
};
```

### **4. 友元函数（Friend Functions）**
- **规则**：友元函数不属于类的成员函数，因此不会被继承。
- **解决方法**：若需在派生类中使用类似功能，需重新声明友元或提供派生类接口。

**示例**：

```cpp
class Base {
    friend void print(const Base& obj); // 友元函数
};

class Derived : public Base { /*...*/ };

void print(const Derived& d) { 
    print(static_cast<const Base&>(d)); // 间接调用基类友元函数
}
```


### **5. 私有成员函数（Private Member Functions）**
- **规则**：私有成员函数对派生类不可见，无法被继承或调用。
- **解决方法**：若需派生类扩展功能，可将函数改为 `protected`。

**示例**：

```cpp
class Base {
protected: // 改为 protected，允许派生类访问
    void helper() { /*...*/ }
};

class Derived : public Base {
public:
    void foo() {
        helper(); // 合法访问
    }
};
```


### **6. 被名字隐藏的函数（Name-Hidden Functions）**
- **规则**：若派生类定义了与基类同名的函数（即使参数不同），基类的所有同名函数会被隐藏。
- **解决方法**：使用 `using Base::func;` 显式引入基类重载。

**示例**：

```cpp
class Base {
public:
    void func(int x) { /*...*/ }
};

class Derived : public Base {
public:
    using Base::func; // 引入基类重载
    void func(double x) { /*...*/ }
};

int main() {
    Derived d;
    d.func(42);   // 调用 Base::func(int)
    d.func(3.14); // 调用 Derived::func(double)
    return 0;
}
```

### **总结：非自动继承的函数类型**

| 函数类型          | 处理方式                     |
|-------------------|------------------------------|
| 构造函数          | 使用 `using` 或显式定义       |
| 析构函数          | 定义虚析构函数                |
| 赋值运算符        | 显式调用基类运算符            |
| 友元函数          | 重新声明或封装                |
| 私有成员函数      | 改为 `protected` 或 `public` |
| 被名字隐藏的函数  | 使用 `using` 声明引入         |

---

## 继承总结
- **继承方式**：控制基类成员在派生类中的访问权限。
- **虚函数与多态**：实现运行时多态，需注意虚析构函数。
- **菱形继承**：通过虚继承解决数据冗余。
- **设计原则**：遵循 LSP，优先组合，谨慎使用多重继承。

合理使用继承能提高代码复用性和扩展性，但需避免滥用导致复杂性和维护成本增加。
