# --- 1. Component (컴포넌트) 인터페이스 ---
class UIElement:
    """
    Component: 모든 요소의 기본 인터페이스입니다. 
    C++의 'Shape' 구조체와 같은 역할.
    """
    def display(self):
        """요소를 화면에 표시하는 기본 동작."""
        raise NotImplementedError

# --- 2. Concrete Component (구체 컴포넌트) ---
class Button(UIElement):
    """
    Concrete Component: 원본 객체입니다. C++의 'Circle'과 같은 역할.
    """
    def __init__(self, label):
        self.label = label
        
    def display(self):
        """기본 버튼 렌더링을 시뮬레이션합니다."""
        return f"[{self.label} Button]"

# --- 3. Decorator (데코레이터) 추상 클래스 ---
class Decorator(UIElement):
    """
    Decorator: UIElement를 감싸는 추상 클래스입니다.
    """
    def __init__(self, element):
        # 감쌀 객체를 포함합니다.
        self._element = element
        
    def display(self):
        # 감싼 객체의 기본 동작을 호출합니다.
        return self._element.display()

# --- 4. Concrete Decorator (구체 데코레이터) ---
class LoggerDecorator(Decorator):
    """
    Concrete Decorator: 원본 버튼에 '로깅' 기능을 추가합니다.
    C++ 슬라이드의 'ColoredShape'와 같은 역할.
    """
    def display(self):
        # 1. 감싼 객체의 기본 동작(버튼 표시)을 호출합니다.
        base_display = self._element.display()
        
        # 2. 새로운 기능(로깅)을 추가합니다.
        log_message = " + LOGGED for UX tracking"
        
        return base_display + log_message

# --- 실행 예시 ---

if __name__ == "__main__":
    
    # 1. 원본 객체 생성
    basic_button = Button("Confirm")
    print("--- 1. 기본 버튼 ---")
    print(basic_button.display()) # [Confirm Button]

    # 2. 로깅 데코레이터로 감싸기
    logged_button = LoggerDecorator(basic_button)
    print("\n--- 2. 기능 확장된 버튼 ---")
    print(logged_button.display()) # [Confirm Button] + LOGGED for UX tracking
    
    # 3. 중첩 데코레이션 (데코레이터 안에 데코레이터를 넣을 수도 있습니다)
    # LoggerDecorator(LoggerDecorator(Button))
    double_logged_button = LoggerDecorator(logged_button)
    print("\n--- 3. 중첩된 기능 확장 ---")
    print(double_logged_button.display()) # [Confirm Button] + LOGGED for UX tracking + LOGGED for UX tracking
