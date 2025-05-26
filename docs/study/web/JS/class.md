# 类

## 概述

### **一、类的定义**

#### 1. **基本语法（ES6+）**

```javascript
class ClassName {
  constructor(/* 参数 */) { /* 初始化逻辑 */ }
  方法名() { /* 实例方法 */ }
  static 静态方法名() { /* 静态方法 */ }
  get 属性名() { /* Getter */ }
  set 属性名(v) { /* Setter */ }
}
```

#### 2. **类表达式**

```javascript
const MyClass = class { /* ... */ };
```

---

### **二、核心特性**
#### 1. **构造函数 `constructor`**
- 每个类只能有一个 `constructor`。
- 实例化时自动调用，用于初始化对象属性。

#### 2. **实例方法**
- 定义在类的原型（`prototype`）上，所有实例共享。
- 通过实例调用：`obj.method()`。

#### 3. **静态方法（`static`）**
- 通过类名直接调用：`ClassName.staticMethod()`。
- 常用于工具函数或类级别操作。

#### 4. **Getter/Setter**
- 提供对属性的访问控制：

  ```javascript
  class User {
    constructor(name) { this._name = name; }
    get name() { return this._name.toUpperCase(); }
    set name(v) { this._name = v; }
  }
  ```

---

### **三、继承**
#### 1. **`extends` 与 `super`**

```javascript
class Student extends Person {
  constructor(name, grade) {
    super(name); // 调用父类构造函数
    this.grade = grade;
  }
}
```

- **`super` 的作用**：
  - 子类构造函数中调用父类构造函数。
  - 子类方法中调用父类方法：`super.parentMethod()`。

#### 2. **方法重写**
- 子类可重写父类方法，通过 `super` 保留父类逻辑。

---

### **四、私有成员（ES2022+）**
#### 1. **私有属性/方法**
- 使用 `#` 前缀声明，仅类内部可访问：

  ```javascript
  class Wallet {
    #balance = 0; // 私有属性
    #log() { /* 私有方法 */ }
  }
  ```

#### 2. **静态私有成员**

```javascript
class Config {
  static #secretKey = "abc123"; // 静态私有属性
}
```

---

### **五、静态成员**
#### 1. **静态属性**

```javascript
class MathUtils {
  static PI = 3.14159; // 静态属性（ES2022+）
}
console.log(MathUtils.PI); // 3.14159
```

#### 2. **静态块（ES2022+）**

```javascript
class MyClass {
  static { /* 类初始化时的逻辑 */ }
}
```

---

### **六、注意事项**
1. **类声明不会提升（Hoisting）**  
   必须先定义类，再实例化。

2. **严格模式**  
   类内部默认启用严格模式。

3. **方法的不可枚举性**  
   类中定义的方法不可通过 `for...in` 遍历。

4. **本质仍是原型继承**  
   `class` 是语法糖，底层基于原型链：

   ```javascript
   class A {}
   console.log(typeof A); // "function"
   ```

---

### **七、对比 ES5 原型写法**

| 特性               | ES6 `class`                          | ES5 原型写法                     |
|--------------------|--------------------------------------|---------------------------------|
| **构造函数**        | `constructor()`                      | `function Class() {}`           |
| **方法定义**        | 直接写在类内部                       | `Class.prototype.method = ...`  |
| **继承**            | `extends` + `super`                  | `Child.prototype = Object.create(Parent.prototype)` |
| **私有成员**        | `#` 前缀                            | 无（约定用 `_`）                |

---

### **八、最佳实践**

1. **优先使用 `class` 语法**：代码更简洁易读。
2. **私有成员用 `#`**：替代 `_` 约定，确保封装性。
3. **避免多层继承**：优先使用组合模式。
4. **静态方法用于工具函数**：如 `Date.now()`。

---

### **九、示例：完整类实现**

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }
  speak() {
    console.log(`${this.name} makes a noise.`);
  }
}

class Dog extends Animal {
  #breed; // 私有属性
  constructor(name, breed) {
    super(name);
    this.#breed = breed;
  }
  speak() {
    super.speak();
    console.log(`${this.name} barks.`);
  }
  static info() {
    console.log("Dogs are loyal!");
  }
}

const dog = new Dog("Buddy", "Golden");
dog.speak(); // "Buddy makes a noise. Buddy barks."
Dog.info();  // "Dogs are loyal!"
```

---

掌握这些知识点后，可以更高效地使用 JavaScript 类进行面向对象开发！ 🚀


