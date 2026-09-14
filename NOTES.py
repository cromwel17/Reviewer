<<<<<<< HEAD
"""
================================================================================
AI ENGINEERING TOPIC-BY-TOPIC EXAM REVIEWER IMPLEMENTATION SUITE
================================================================================
Modules Covered:
  - Module 1: Python Software Engineering & OOP Architecture
  - Module 2: Data Pipelines & Vectorized Computation
  - Module 3: Vector Embeddings, Evaluation & Token Budgeting
"""

import math
import random
import logging
import datetime
from abc import ABC, abstractmethod
from functools import wraps

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


# ==============================================================================
# MODULE 1: PYTHON SOFTWARE ENGINEERING & OOP ARCHITECTURE
# ==============================================================================

# ------------------------------------------------------------------------------
# Topic 1: Custom Exception Handling & System Resiliency
# ------------------------------------------------------------------------------
class BookUnavailableError(Exception):
    """Raised when an item cannot be checked out because it is already on loan."""
    def __init__(self, title: str):
        self.title = title
        super().__init__(f"The book '{self.title}' is currently unavailable for loan.")


def safe_api_retry(func, max_retries: int = 3):
    """Executes a function with retry resilience targeting specific transient ConnectionErrors."""
    for attempt in range(1, max_retries + 1):
        try:
            return func()
        except ConnectionError as err:
            logging.warning(f"Attempt {attempt}/{max_retries} failed: {err}")
            if attempt == max_retries:
                raise RuntimeError(f"Operation failed after maximum retry limit ({max_retries}).") from err


# ------------------------------------------------------------------------------
# Topic 2: Abstract Base Classes (ABCs) & Polymorphism
# ------------------------------------------------------------------------------
class Shape(ABC):
    """Abstract Base Class enforcing unified geometric interface contract across implementations."""
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be a positive non-zero number.")
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive non-zero numbers.")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


def calculate_total_area(shapes: list[Shape]) -> float:
    """Polymorphic execution calling .area() across varied child instances dynamically."""
    return sum(shape.area() for shape in shapes)


# ------------------------------------------------------------------------------
# Topic 3: Class vs. Instance Attributes & Factory Methods
# ------------------------------------------------------------------------------
class Employee:
    # Class attribute: Shared across all class instances in memory
    tax_rate: float = 0.20

    def __init__(self, name: str, base_salary: float):
        # Instance attributes: Unique per individual object instance
        self.name = name
        self.base_salary = base_salary

    def net_pay(self) -> float:
        return self.base_salary * (1.0 - Employee.tax_rate)

    @classmethod
    def from_dict(cls, data: dict):
        """Factory constructor instantiating an object from raw key-value dictionary data."""
        return cls(name=data["name"], base_salary=data["base_salary"])


# ------------------------------------------------------------------------------
# Topic 4: Higher-Order Functions & Metadata Preservation
# ------------------------------------------------------------------------------
def log_execution(func):
    """Decorator tracking execution timestamp and preserving function metadata via @wraps."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = func(*args, **kwargs)
        print(f"[{timestamp}] Function '{func.__name__}' executed | Args: {args} | Return: {result}")
        return result
    return wrapper


@log_execution
def compute_grade(score: float) -> str:
    """Evaluates numeric score into standard letter grade."""
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"


# ==============================================================================
# MODULE 2: DATA PIPELINES & VECTORIZED COMPUTATION
# ==============================================================================

# ------------------------------------------------------------------------------
# Topic 5: Data Cleaning & Preprocessing Workflow
# ------------------------------------------------------------------------------
def clean_survey_data(raw_records: list[dict]) -> pd.DataFrame:
    """Transforms noisy survey inputs via normalization, imputation, and deduplication."""
    df = pd.DataFrame(raw_records)
    
    # 1. Text Normalization: trim whitespace and lowercase values
    df["response"] = df["response"].astype(str).str.strip().str.lower()
    
    # 2. Missing Value Imputation: fill missing numeric values with column mean
    df["age"] = df["age"].fillna(df["age"].mean())
    
    # 3. Deduplication: drop identical duplicate rows
    df = df.drop_duplicates().reset_index(drop=True)
    
    return df


# ------------------------------------------------------------------------------
# Topic 6: Vectorized Computation vs. Iterative Loops
# ------------------------------------------------------------------------------
def curve_scores_vectorized(scores: np.ndarray, curve_points: float = 5.0, max_cap: float = 100.0) -> np.ndarray:
    """Applies vectorized broadcasting addition and upper bounding via np.clip."""
    return np.clip(scores + curve_points, a_min=None, a_max=max_cap)


# ==============================================================================
# MODULE 3: VECTOR EMBEDDINGS, EVALUATION & TOKEN BUDGETING
# ==============================================================================

# ------------------------------------------------------------------------------
# Topic 7: Vector Similarity & Retrieval Matching
# ------------------------------------------------------------------------------
def compute_cosine_similarity(vec_a: np.ndarray, vec_b: np.ndarray) -> float:
    """
    Computes Cosine Similarity between two 1D vectors:
    Cosine Similarity = (a . b) / (||a|| * ||b||)
    """
    dot_product = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)


# ------------------------------------------------------------------------------
# Topic 8: Model Evaluation & Metric Selection Strategies
# ------------------------------------------------------------------------------
def evaluate_binary_classifier(y_true: list[str], y_pred: list[str], pos_label: str = "spam") -> dict:
    """Calculates Confusion Matrix, Precision, Recall, and F1-Score for target classification."""
    cm = confusion_matrix(y_true, y_pred, labels=["ham", pos_label])
    prec = precision_score(y_true, y_pred, pos_label=pos_label)
    rec = recall_score(y_true, y_pred, pos_label=pos_label)
    f1 = f1_score(y_true, y_pred, pos_label=pos_label)
    
    return {
        "confusion_matrix": cm,
        "precision": prec,
        "recall": rec,
        "f1_score": f1
    }


# ------------------------------------------------------------------------------
# Topic 9: Token Budgeting & Context Window Management
# ------------------------------------------------------------------------------
def validate_token_budget(text_chunks: list[str], max_context: int = 8000, reserved_output: int = 1000) -> int:
    """
    Estimates token count using the heuristic (1 token ~ 4 chars).
    Raises ValueError if cumulative context exceeds available context capacity.
    """
    capacity = max_context - reserved_output
    estimated_tokens = sum(math.ceil(len(chunk) / 4.0) for chunk in text_chunks)
    
    if estimated_tokens > capacity:
        overflow = estimated_tokens - capacity
        raise ValueError(
            f"Token limit exceeded! Required: {estimated_tokens}, Capacity: {capacity} (Exceeded by {overflow})."
        )
    
    return estimated_tokens


# ==============================================================================
# INTEGRATED VERIFICATION SUITE
# ==============================================================================
if __name__ == "__main__":
    print("================================================================================")
    print("EXECUTING REVIEWER MODULE TEST SUITE")
    print("================================================================================\n")

    # Topic 1 Verification
    print("--- Topic 1: Custom Exception Handling ---")
    try:
        raise BookUnavailableError("Designing Data-Intensive Applications")
    except BookUnavailableError as e:
        print(f"Caught Custom Exception: {e}")

    # Topic 2 Verification
    print("\n--- Topic 2: ABC & Polymorphism ---")
    shapes_list: list[Shape] = [Circle(5.0), Rectangle(4.0, 6.0)]
    print(f"Polymorphic Total Area: {calculate_total_area(shapes_list):.2f}")

    # Topic 3 Verification
    print("\n--- Topic 3: Class vs. Instance Attributes ---")
    emp = Employee.from_dict({"name": "Alice", "base_salary": 100000.0})
    print(f"Initial Net Pay (20% Default Tax): ${emp.net_pay():,.2f}")
    Employee.tax_rate = 0.25
    print(f"Updated Net Pay (25% Class Tax Update): ${emp.net_pay():,.2f}")

    # Topic 4 Verification
    print("\n--- Topic 4: Logging Decorator & Wraps ---")
    compute_grade(88.5)
    print(f"Preserved Metadata Name: {compute_grade.__name__}")

    # Topic 5 Verification
    print("\n--- Topic 5: Pandas Data Cleaning Pipeline ---")
    raw_data = [
        {"response": " Yes ", "age": 20.0},
        {"response": "YES", "age": None},
        {"response": " Yes ", "age": 20.0}
    ]
    cleaned_df = clean_survey_data(raw_data)
    print(cleaned_df)

    # Topic 6 Verification
    print("\n--- Topic 6: Vectorized Operations ---")
    raw_scores = np.array([55, 78, 98])
    print(f"Original: {raw_scores} | Curved & Capped: {curve_scores_vectorized(raw_scores)}")

    # Topic 7 Verification
    print("\n--- Topic 7: Cosine Similarity ---")
    vec1 = np.array([1.0, 2.0, 3.0])
    vec2 = np.array([1.0, 2.0, 2.9])
    print(f"Calculated Cosine Similarity: {compute_cosine_similarity(vec1, vec2):.4f}")

    # Topic 8 Verification
    print("\n--- Topic 8: Classifier Metrics ---")
    ground_truth = ["spam", "ham", "spam", "ham", "spam"]
    predictions  = ["spam", "ham", "ham",  "ham", "spam"]
    results = evaluate_binary_classifier(ground_truth, predictions)
    print(f"Precision: {results['precision']:.2f} | Recall: {results['recall']:.2f} | F1: {results['f1_score']:.2f}")

    # Topic 9 Verification
    print("\n--- Topic 9: Token Budget Guardrail ---")
    sample_text = ["Standard vector embedding text chunk. " * 10 for _ in range(5)]
    tokens_used = validate_token_budget(sample_text, max_context=4000, reserved_output=500)
    print(f"Estimated Tokens Used: {tokens_used} / 3500 Available Capacity Limit")
=======
"""
================================================================================
AI ENGINEERING TOPIC-BY-TOPIC EXAM REVIEWER IMPLEMENTATION SUITE
================================================================================
Modules Covered:
  - Module 1: Python Software Engineering & OOP Architecture
  - Module 2: Data Pipelines & Vectorized Computation
  - Module 3: Vector Embeddings, Evaluation & Token Budgeting
"""

import math
import random
import logging
import datetime
from abc import ABC, abstractmethod
from functools import wraps

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


# ==============================================================================
# MODULE 1: PYTHON SOFTWARE ENGINEERING & OOP ARCHITECTURE
# ==============================================================================

# ------------------------------------------------------------------------------
# Topic 1: Custom Exception Handling & System Resiliency
# ------------------------------------------------------------------------------
class BookUnavailableError(Exception):
    """Raised when an item cannot be checked out because it is already on loan."""
    def __init__(self, title: str):
        self.title = title
        super().__init__(f"The book '{self.title}' is currently unavailable for loan.")


def safe_api_retry(func, max_retries: int = 3):
    """Executes a function with retry resilience targeting specific transient ConnectionErrors."""
    for attempt in range(1, max_retries + 1):
        try:
            return func()
        except ConnectionError as err:
            logging.warning(f"Attempt {attempt}/{max_retries} failed: {err}")
            if attempt == max_retries:
                raise RuntimeError(f"Operation failed after maximum retry limit ({max_retries}).") from err


# ------------------------------------------------------------------------------
# Topic 2: Abstract Base Classes (ABCs) & Polymorphism
# ------------------------------------------------------------------------------
class Shape(ABC):
    """Abstract Base Class enforcing unified geometric interface contract across implementations."""
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be a positive non-zero number.")
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive non-zero numbers.")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


def calculate_total_area(shapes: list[Shape]) -> float:
    """Polymorphic execution calling .area() across varied child instances dynamically."""
    return sum(shape.area() for shape in shapes)


# ------------------------------------------------------------------------------
# Topic 3: Class vs. Instance Attributes & Factory Methods
# ------------------------------------------------------------------------------
class Employee:
    # Class attribute: Shared across all class instances in memory
    tax_rate: float = 0.20

    def __init__(self, name: str, base_salary: float):
        # Instance attributes: Unique per individual object instance
        self.name = name
        self.base_salary = base_salary

    def net_pay(self) -> float:
        return self.base_salary * (1.0 - Employee.tax_rate)

    @classmethod
    def from_dict(cls, data: dict):
        """Factory constructor instantiating an object from raw key-value dictionary data."""
        return cls(name=data["name"], base_salary=data["base_salary"])


# ------------------------------------------------------------------------------
# Topic 4: Higher-Order Functions & Metadata Preservation
# ------------------------------------------------------------------------------
def log_execution(func):
    """Decorator tracking execution timestamp and preserving function metadata via @wraps."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = func(*args, **kwargs)
        print(f"[{timestamp}] Function '{func.__name__}' executed | Args: {args} | Return: {result}")
        return result
    return wrapper


@log_execution
def compute_grade(score: float) -> str:
    """Evaluates numeric score into standard letter grade."""
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"


# ==============================================================================
# MODULE 2: DATA PIPELINES & VECTORIZED COMPUTATION
# ==============================================================================

# ------------------------------------------------------------------------------
# Topic 5: Data Cleaning & Preprocessing Workflow
# ------------------------------------------------------------------------------
def clean_survey_data(raw_records: list[dict]) -> pd.DataFrame:
    """Transforms noisy survey inputs via normalization, imputation, and deduplication."""
    df = pd.DataFrame(raw_records)
    
    # 1. Text Normalization: trim whitespace and lowercase values
    df["response"] = df["response"].astype(str).str.strip().str.lower()
    
    # 2. Missing Value Imputation: fill missing numeric values with column mean
    df["age"] = df["age"].fillna(df["age"].mean())
    
    # 3. Deduplication: drop identical duplicate rows
    df = df.drop_duplicates().reset_index(drop=True)
    
    return df


# ------------------------------------------------------------------------------
# Topic 6: Vectorized Computation vs. Iterative Loops
# ------------------------------------------------------------------------------
def curve_scores_vectorized(scores: np.ndarray, curve_points: float = 5.0, max_cap: float = 100.0) -> np.ndarray:
    """Applies vectorized broadcasting addition and upper bounding via np.clip."""
    return np.clip(scores + curve_points, a_min=None, a_max=max_cap)


# ==============================================================================
# MODULE 3: VECTOR EMBEDDINGS, EVALUATION & TOKEN BUDGETING
# ==============================================================================

# ------------------------------------------------------------------------------
# Topic 7: Vector Similarity & Retrieval Matching
# ------------------------------------------------------------------------------
def compute_cosine_similarity(vec_a: np.ndarray, vec_b: np.ndarray) -> float:
    """
    Computes Cosine Similarity between two 1D vectors:
    Cosine Similarity = (a . b) / (||a|| * ||b||)
    """
    dot_product = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)


# ------------------------------------------------------------------------------
# Topic 8: Model Evaluation & Metric Selection Strategies
# ------------------------------------------------------------------------------
def evaluate_binary_classifier(y_true: list[str], y_pred: list[str], pos_label: str = "spam") -> dict:
    """Calculates Confusion Matrix, Precision, Recall, and F1-Score for target classification."""
    cm = confusion_matrix(y_true, y_pred, labels=["ham", pos_label])
    prec = precision_score(y_true, y_pred, pos_label=pos_label)
    rec = recall_score(y_true, y_pred, pos_label=pos_label)
    f1 = f1_score(y_true, y_pred, pos_label=pos_label)
    
    return {
        "confusion_matrix": cm,
        "precision": prec,
        "recall": rec,
        "f1_score": f1
    }


# ------------------------------------------------------------------------------
# Topic 9: Token Budgeting & Context Window Management
# ------------------------------------------------------------------------------
def validate_token_budget(text_chunks: list[str], max_context: int = 8000, reserved_output: int = 1000) -> int:
    """
    Estimates token count using the heuristic (1 token ~ 4 chars).
    Raises ValueError if cumulative context exceeds available context capacity.
    """
    capacity = max_context - reserved_output
    estimated_tokens = sum(math.ceil(len(chunk) / 4.0) for chunk in text_chunks)
    
    if estimated_tokens > capacity:
        overflow = estimated_tokens - capacity
        raise ValueError(
            f"Token limit exceeded! Required: {estimated_tokens}, Capacity: {capacity} (Exceeded by {overflow})."
        )
    
    return estimated_tokens


# ==============================================================================
# INTEGRATED VERIFICATION SUITE
# ==============================================================================
if __name__ == "__main__":
    print("================================================================================")
    print("EXECUTING REVIEWER MODULE TEST SUITE")
    print("================================================================================\n")

    # Topic 1 Verification
    print("--- Topic 1: Custom Exception Handling ---")
    try:
        raise BookUnavailableError("Designing Data-Intensive Applications")
    except BookUnavailableError as e:
        print(f"Caught Custom Exception: {e}")

    # Topic 2 Verification
    print("\n--- Topic 2: ABC & Polymorphism ---")
    shapes_list: list[Shape] = [Circle(5.0), Rectangle(4.0, 6.0)]
    print(f"Polymorphic Total Area: {calculate_total_area(shapes_list):.2f}")

    # Topic 3 Verification
    print("\n--- Topic 3: Class vs. Instance Attributes ---")
    emp = Employee.from_dict({"name": "Alice", "base_salary": 100000.0})
    print(f"Initial Net Pay (20% Default Tax): ${emp.net_pay():,.2f}")
    Employee.tax_rate = 0.25
    print(f"Updated Net Pay (25% Class Tax Update): ${emp.net_pay():,.2f}")

    # Topic 4 Verification
    print("\n--- Topic 4: Logging Decorator & Wraps ---")
    compute_grade(88.5)
    print(f"Preserved Metadata Name: {compute_grade.__name__}")

    # Topic 5 Verification
    print("\n--- Topic 5: Pandas Data Cleaning Pipeline ---")
    raw_data = [
        {"response": " Yes ", "age": 20.0},
        {"response": "YES", "age": None},
        {"response": " Yes ", "age": 20.0}
    ]
    cleaned_df = clean_survey_data(raw_data)
    print(cleaned_df)

    # Topic 6 Verification
    print("\n--- Topic 6: Vectorized Operations ---")
    raw_scores = np.array([55, 78, 98])
    print(f"Original: {raw_scores} | Curved & Capped: {curve_scores_vectorized(raw_scores)}")

    # Topic 7 Verification
    print("\n--- Topic 7: Cosine Similarity ---")
    vec1 = np.array([1.0, 2.0, 3.0])
    vec2 = np.array([1.0, 2.0, 2.9])
    print(f"Calculated Cosine Similarity: {compute_cosine_similarity(vec1, vec2):.4f}")

    # Topic 8 Verification
    print("\n--- Topic 8: Classifier Metrics ---")
    ground_truth = ["spam", "ham", "spam", "ham", "spam"]
    predictions  = ["spam", "ham", "ham",  "ham", "spam"]
    results = evaluate_binary_classifier(ground_truth, predictions)
    print(f"Precision: {results['precision']:.2f} | Recall: {results['recall']:.2f} | F1: {results['f1_score']:.2f}")

    # Topic 9 Verification
    print("\n--- Topic 9: Token Budget Guardrail ---")
    sample_text = ["Standard vector embedding text chunk. " * 10 for _ in range(5)]
    tokens_used = validate_token_budget(sample_text, max_context=4000, reserved_output=500)
    print(f"Estimated Tokens Used: {tokens_used} / 3500 Available Capacity Limit")
>>>>>>> 5d9d7df144b35758ba08b64d4eefbbecf05e51fd
