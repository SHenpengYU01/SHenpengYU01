# 设计模式

此部分包含一些设计模式的总结，参考《大话设计模式（程杰著）》，多数内容来源于AI总结。

## 工厂模式

## 装饰策略


装饰设计模式（Decorator Pattern）是一种**结构型设计模式**，允许动态地向对象添加新功能，且不改变其原有结构。它通过将对象包装在装饰器类中，以**组合替代继承**的方式扩展功能，避免了类数目爆炸问题。

### **核心思想**
1. **动态扩展**：运行时灵活添加或移除功能。
2. **透明性**：装饰后的对象与原对象接口一致，对客户端透明。
3. **组合优先**：用对象组合替代类继承，降低耦合。

---

### **模式结构**

```plaintext
                +---------------------+
                |    Component        |
                +---------------------+
                | + operation():void |
                +---------------------+
                          ▲
             ____________/ \___________
            /                          \
           /                            \
+---------------------+         +---------------------+
|  ConcreteComponent  |         |    Decorator        |
+---------------------+         +---------------------+
| + operation():void  |         | - component:Component|
+---------------------+         | + operation():void   |
                                +---------------------+
                                          ▲
                               __________/ \___________
                              /                        \
                             /                          \
                    +-----------------+         +-----------------+
                    | ConcreteDecoratorA |       | ConcreteDecoratorB |
                    +-----------------+         +-----------------+
                    | + operation():void|       | + operation():void|
                    | + addedBehavior() |       | + addedBehavior() |
                    +-----------------+         +-----------------+
```

- **`Component`**：定义对象接口，可以是抽象类或接口。
- **`ConcreteComponent`**：实现基础功能的具体类。
- **`Decorator`**：继承/实现 `Component`，并持有 `Component` 对象的引用。
- **`ConcreteDecorator`**：具体装饰器，添加额外功能。

---

### **C++ 实现示例**
#### **场景：咖啡店订单系统**
- **基础咖啡（`ConcreteComponent`）**：黑咖啡（`BlackCoffee`）。
- **装饰器（`Decorator`）**：添加牛奶（`MilkDecorator`）、糖（`SugarDecorator`）。

```cpp
#include <iostream>
#include <string>
#include <memory>

// 抽象组件：咖啡接口
class Coffee {
public:
    virtual ~Coffee() = default;
    virtual std::string getDescription() const = 0;
    virtual double cost() const = 0;
};

// 具体组件：黑咖啡
class BlackCoffee : public Coffee {
public:
    std::string getDescription() const override {
        return "Black Coffee";
    }

    double cost() const override {
        return 2.0;
    }
};

// 抽象装饰器
class CoffeeDecorator : public Coffee {
protected:
    std::unique_ptr<Coffee> coffee;
public:
    CoffeeDecorator(std::unique_ptr<Coffee> coffee) : coffee(std::move(coffee)) {}
    std::string getDescription() const override { return coffee->getDescription(); }
    double cost() const override { return coffee->cost(); }
};

// 具体装饰器：添加牛奶
class MilkDecorator : public CoffeeDecorator {
public:
    MilkDecorator(std::unique_ptr<Coffee> coffee) : CoffeeDecorator(std::move(coffee)) {}

    std::string getDescription() const override {
        return coffee->getDescription() + ", Milk";
    }

    double cost() const override {
        return coffee->cost() + 0.5;
    }
};

// 具体装饰器：添加糖
class SugarDecorator : public CoffeeDecorator {
public:
    SugarDecorator(std::unique_ptr<Coffee> coffee) : CoffeeDecorator(std::move(coffee)) {}

    std::string getDescription() const override {
        return coffee->getDescription() + ", Sugar";
    }

    double cost() const override {
        return coffee->cost() + 0.2;
    }
};

int main() {
    // 创建基础咖啡
    auto coffee = std::make_unique<BlackCoffee>();
    std::cout << "Base: " << coffee->getDescription() 
              << ", Cost: $" << coffee->cost() << std::endl;

    // 动态添加牛奶和糖
    auto milkCoffee = std::make_unique<MilkDecorator>(std::move(coffee));
    auto sweetMilkCoffee = std::make_unique<SugarDecorator>(std::move(milkCoffee));

    std::cout << "Decorated: " << sweetMilkCoffee->getDescription()
              << ", Cost: $" << sweetMilkCoffee->cost() << std::endl;

    return 0;
}
```

- **输出结果**

```plaintext
Base: Black Coffee, Cost: $2
Decorated: Black Coffee, Milk, Sugar, Cost: $2.7
```


### **装饰模式的优势**

| 优势 | 说明 |
|------|------|
| **灵活扩展** | 动态添加功能，无需修改原有代码 |
| **避免类爆炸** | 替代多层次的继承结构 |
| **单一职责原则** | 每个装饰器只关注一个功能 |
| **开闭原则** | 对扩展开放，对修改关闭 |


### **适用场景**
1. **动态添加功能**：如 GUI 控件添加边框、滚动条。
2. **撤销功能**：通过装饰器记录对象状态变化。
3. **日志或权限校验**：为方法调用添加额外逻辑（类似中间件）。

---

### **注意事项**
1. **复杂度控制**：装饰器过多会导致代码难以维护。
2. **初始化顺序**：装饰器的包装顺序可能影响最终行为。
3. **性能开销**：多层装饰可能增加微小性能损耗。

---

### **与其他模式对比**

| 模式         | 核心区别                    |
|--------------|----------------------------|
| **适配器**   | 改变接口，装饰器保持接口一致 |
| **组合**     | 装饰器是组合的特例（单组件）|
| **策略**     | 装饰器扩展功能，策略替换算法 |





