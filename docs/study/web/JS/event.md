# 事件

!!! note "备注"
     web 事件不是 JavaScript 语言的核心——它们被定义成内置于浏览器的 API。JavaScript 在不同环境下使用不同的事件模型。

## 事件处理器

- 使用addEventListener()添加事件处理器
- 使用removeEventListener()移除事件处理器

button可添加的事件：focus/blur, click, dblclick, mouseover/mouseout

可多次使用addEventListener为事件添加多个处理器。

### 事件处理器属性

可以触发事件的对象（如按钮）通常也有属性，其名称是 on，后面是事件的名称。为了监听事件，可以将处理函数分配给该属性。每个属性只会接受赋值给他的处理函数，后续赋值会覆盖前面赋值，因此事件处理器属性不能为一个事件添加多个处理函数。
例：

```js
const btn = document.querySelector("button");

function random(number) {
  return Math.floor(Math.random() * (number + 1));
}

btn.onclick = () => {
  const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})`;
  document.body.style.backgroundColor = rndCol;
};
```

## 事件对象

在事件处理函数内部，可能会有一个固定指定名称的参数，例如 event、evt 或 e。这被称为事件对象，它被自动传递给事件处理函数，以提供额外的功能和信息。

```js
const btn = document.querySelector("button");

function random(number) {
  return Math.floor(Math.random() * (number + 1));
}

function bgChange(e) {
  const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})`;
  e.target.style.backgroundColor = rndCol;
  console.log(e);
}

btn.addEventListener("click", bgChange);
```

事件对象 e 的 target 属性始终是事件刚刚发生的元素的引用。这会改变按钮的颜色，而不是页面背景。


## 事件冒泡

事件冒泡描述了浏览器如何处理针对嵌套元素的事件。

### **一、事件冒泡的定义**
#### 1. **核心概念**
> 事件冒泡是 DOM 事件传播的一种机制，指事件从 **触发事件的元素（目标元素）** 开始，逐级向上（向父元素）传播到文档根节点（`window`）的过程。  
> —— [MDN: Event Bubbling](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#event_bubbling)

#### 2. **事件传播三阶段**
1. **捕获阶段（Capture Phase）**：事件从根节点向下传递到目标元素。  
2. **目标阶段（Target Phase）**：事件到达目标元素。  
3. **冒泡阶段（Bubble Phase）**：事件从目标元素向上冒泡到根节点。  

---

### **二、事件冒泡的示例**
#### 1. **HTML 结构**
```html
<div id="grandparent">
  <div id="parent">
    <button id="child">Click Me</button>
  </div>
</div>
```

#### 2. **事件监听与冒泡**
```javascript
document.getElementById("grandparent").addEventListener("click", () => {
  console.log("Grandparent clicked");
});

document.getElementById("parent").addEventListener("click", () => {
  console.log("Parent clicked");
});

document.getElementById("child").addEventListener("click", () => {
  console.log("Child clicked");
});

// 点击按钮后的输出顺序：
// "Child clicked" → "Parent clicked" → "Grandparent clicked"
```

---

### **三、事件冒泡的应用**
#### 1. **事件委托（Event Delegation）**
- **原理**：利用冒泡机制，在父元素上统一处理子元素的事件。
- **优势**：减少事件监听器数量，支持动态添加的子元素。
- **示例**：
  ```javascript
  document.querySelector("#parent").addEventListener("click", (event) => {
    if (event.target.tagName === "BUTTON") {
      console.log("Button clicked:", event.target.textContent);
    }
  });
  ```

#### 2. **阻止事件冒泡**
- **方法**：调用 `event.stopPropagation()`。
- **场景**：阻止事件继续向上传播。
  ```javascript
  document.getElementById("child").addEventListener("click", (event) => {
    console.log("Child clicked");
    event.stopPropagation(); // 阻止冒泡
  });
  // 点击按钮后只输出 "Child clicked"
  ```

---

### **四、事件冒泡与事件捕获的对比**
| 特性               | 事件冒泡（Bubbling）          | 事件捕获（Capture）             |
|--------------------|-----------------------------|--------------------------------|
| **传播方向**        | 目标元素 → 根节点            | 根节点 → 目标元素               |
| **监听器注册方式**  | `addEventListener(type, handler)`（默认） | `addEventListener(type, handler, true)` |
| **执行顺序**        | 在目标阶段后执行             | 在目标阶段前执行                |

---

### **五、关键注意事项**
1. **并非所有事件都冒泡**  
   如 `focus`、`blur` 等事件不会冒泡，需使用捕获阶段或直接监听目标元素。

2. **`event.target` vs `event.currentTarget`**  
   - `event.target`：触发事件的原始元素（如点击的按钮）。  
   - `event.currentTarget`：当前处理事件的元素（如绑定监听器的父元素）。  

3. **停止冒泡的副作用**  
   过度使用 `event.stopPropagation()` 可能破坏其他监听器逻辑，需谨慎使用。

---

### **六、总结**
- **事件冒泡**是 DOM 事件模型的默认传播机制，适合实现事件委托等高效模式。  
- 通过 `event.stopPropagation()` 可控制冒泡行为。  
- 结合捕获和冒泡机制，可灵活管理复杂的事件交互。  




