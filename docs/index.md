# Welcome to Cool Tea's Site

This is the homepage.

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## Others

### Code block

```c title='printf.c'
int a=10;
printf("Hello World!");
```

### Math

$$
f(x) = \int_{-\infty}^\infty
    \hat f(\xi)\,e^{2 \pi i \xi x}
    \,d\xi
$$

### Expandable note

<details><summary>点击展开</summary>内容</details>

??? note "an easy note"
    here is how the note tag is implemented.

??? warning "a warning"
    This is a warning

!!! info "选项卡示例"
    选项卡内容
    ```python
    def hello():
        print("Hello, world!")
    ```
??? info "选项卡info"
    选项卡内容
    ```python
    def hello():
        print("Hello, world!")
    ```


### footnotes

这是一个带脚注的句子[^1]。  
haafasdfeafesdfajjjakadfa;faeipfhawke


[^1]: 这是脚注的内容。

### Tasklist

- [x] 已完成任务
- [ ] 未完成任务

[![Built with Material for MkDocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?style=for-the-badge&logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)

