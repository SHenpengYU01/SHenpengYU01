# 初始化参数列表（initializer list）

在 C++ 中，**初始化列表（Initialization List）** 是构造函数中用于直接初始化类成员变量的一种机制。它在构造函数的参数列表后以冒号（`:`）开头，后跟成员变量的初始化表达式。通过初始化列表，成员变量在对象创建时被直接初始化，而不是先默认初始化再赋值。以下是关于初始化列表的详细说明：



## **一、初始化列表的语法**

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



## **二、初始化列表的用途**
### 1. **初始化 `const` 成员**

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

### 2. **初始化引用成员**

- 引用成员必须在声明时绑定到某个变量，也**只能通过初始化列表**完成。

   ```cpp
   class RefExample {
   public:
       RefExample(int& ref) : refMember(ref) {} // 正确
   private:
       int& refMember;
   };
   ```

### 3. **初始化没有默认构造函数的类成员**

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

### 4. **提升效率**
- 对于非基本类型（如类对象），使用初始化列表直接调用**拷贝构造函数**，比在构造函数体内先默认构造再赋值更高效。

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



## **三、初始化列表的注意事项**
### 1. **初始化顺序**
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

!!! note "例子"
    下面是一个有关初始化顺序的实际例子：

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
    这里实现Vector的拷贝构造函数。在初始化列表中，类中先被声明的`m_pElements` 却依赖于类中在它后面声明的 `m_nCapacity`，这大概率会导致`new`为`m_pElements`分配的内存大小出错。
    所以最好不要让初始化参数列表中的参数初始化相互耦合，即使耦合也要让初始化顺序符合声明顺序。  


### 2. **默认初始化**
- 未在初始化列表中显式初始化的成员变量：
  - 基本类型（如 `int`、`double`）会执行默认初始化（值不确定）。
  - 类类型会调用默认构造函数。若类没有默认构造函数，**必须**通过初始化列表显式初始化。



## **四、继承中的初始化列表**
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

## **五、类内成员初始化（C++11 起）**
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

## **六、总结**

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
