## Software Design Pattern - Decorator

This repository contains the Python implementation of the **Decorator Pattern** for a university assignment on Software Design Patterns.

### 1. Project Objective

* **Pattern:** **Decorator Pattern** (장식자 패턴)

* **Goal:** To demonstrate **dynamic feature extension** in UI components. The primary goal is to add functionality (like logging) to the base component (`Button`) without modifying its original source code. This is key for scalable UI/UX component design.

### 2. Code Structure (`ui_decorator.py`)

The file `ui_decorator.py` implements the four core components of the pattern:

* **`UIElement`:** The **Component** interface (the common contract).

* **`Button`:** The **Concrete Component** (the original UI element).

* **`Decorator`:** The abstract **Decorator** class (holds the reference to the wrapped object).

* **`LoggerDecorator`:** The **Concrete Decorator** (the object that wraps the button to add the logging feature).

### 3. Execution Instructions

Run the Python file directly in your terminal:

```bash
ui_decorator.py
