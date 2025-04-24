# Test

The following are some tests of what material can show.  

## Code block

```c title='printf.c' linenums="1"
int a=10; // (1)
printf("Hello World!");
```

1.  :a is a int

``` yaml hl_lines="2"
theme:
  features:
    - content.code.annotate # (1)
```

1.  :man_raising_hand: I'm a code annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be written in Markdown.
## Math

$$
f(x) = \int_{-\infty}^\infty
    \hat f(\xi)\,e^{2 \pi i \xi x}
    \,d\xi
$$

## Expandable note

<details><summary>implemented with HTNL</summary>contents</details>

??? note "an easy note"
    here is how the note tag is implemented.

??? warning "a warning"
    This is a warning

!!! info "Info"
    Info content
    ```python
    def hello():
        print("Hello, world!")
    ```
??? info "foldable info"
    Info content
    ```python
    def hello():
        print("Hello, world!")
    ```
??? question "why"
    why?
## footnotes

Sentence with footnote[^1]。  

[^1]: This is the footnote content

## Tasklist

- [x] done
- [ ] to be done


## Image

<figure markdown="span">
  ![Image title](img/study/math/linear%20algebra/dian.png){ width="400" }
  <figcaption>Liner algebra</figcaption>
</figure>


## Emoji

:cry:
:smile:
:fontawesome-brands-youtube:{ .youtube }

:fontawesome-solid-face-sad-cry:
:smirk:
:no-mouth:
:+1:
:-1:
:thinking:
:hugs:
[:yum:](https://tasty.co/)
:kissing_heart:


## Grids

<div class="grid cards" markdown>

- [:fontawesome-brands-html5: __HTML__ for content and structure](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [:fontawesome-brands-js: __JavaScript__ for interactivity](https://www.w3schools.com/Css/)
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... ~~huh~~?

</div>

## Format

- ++tab++
- ^^underline^^
- ==highlight==
- ~~delete~~
- ^up^
- ~down~

```md
++tab++
^^underline^^
==highlight==
^up^
~down~
```

[![Built with Material for MkDocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?style=for-the-badge&logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)
