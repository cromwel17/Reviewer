"""
================================================================================
AI ENGINEERING EXAM REVIEWER & CHEAT SHEET (MODULES 1 - 3)
================================================================================
This repository section contains all problem solutions from Set A and Set B,
fully implemented, typed, and commented. Run this script directly to test all
implementations end-to-end.
"""

import math
import random
import logging
import datetime
from abc import ABC, abstractmethod
from functools import wraps

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


# ==============================================================================
# SET A — PROBLEM 1: LIBRARY LOAN TRACKER (OOP & CUSTOM EXCEPTIONS)
# ==============================================================================

class BookUnavailableError(Exception):
    """
    Custom exception raised when attempting to borrow a book that is checked out.
    Inheriting from Exception allows specific upstream handling[cite: 1].
    """
    def __init__(self, title: str):
        self.title = title
        super().__init__(f"The book '{self.title}' is currently unavailable for loan.")


class Book:
    def __init__(self, title: str, isbn: str, is_checked_out: bool = False):
        self.title = title
        self.isbn = isbn
        self.is_checked_out = is_checked_out

    def __str__(self) -> str:
        """Human-readable representation showing title and current status[cite: 1]."""
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"'{self.title}' (ISBN: {self.isbn}) — [{status}]"


class Member:
    def __init__(self, name: str):
        self.name = name

    def borrow(self, book: Book) -> None:
        if book.is_checked_out:
            raise BookUnavailableError(book.title)
        book.is_checked_out = True
        print(f"[{self.name}] Successfully borrowed: '{book.title}'")

    def return_book(self, book: Book) -> None:
        book.is_checked_out = False
        print(f"[{self.name}] Successfully returned: '{book.title}'")


# ==============================================================================
# SET A — PROBLEM 2: SHAPE HIERARCHY WITH A TWIST (ABC & POLYMORPHISM)
# ==============================================================================

class Shape(ABC):
    """
    Abstract Base Class enforcing interface rules across all child shapes[cite: 1].
    Attempting to instantiate Shape directly will raise TypeError[cite: 1].
    """
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError(f"Invalid dimension: radius={radius} must be positive.")
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if width <= 0:
            raise ValueError(f"Invalid dimension: width={width} must be positive.")
        if height <= 0:
            raise ValueError(f"Invalid dimension: height={height} must be positive.")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError(f"Invalid dimensions: sides ({side_a}, {side_b}, {side_c}) must be positive.")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self) -> float:
        # Heron's Formula
        s = (self.side_a + self.side_b + self.side_c) / 2.0
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c


def total_area(shapes: list[Shape]) -> float:
    """Polymorphic sum: calls .area() uniformly across different shape types[cite: 1]."""
    return sum(shape.area() for shape in shapes)


# ==============================================================================
# SET A — PROBLEM 3: RETRY-SAFE API CALLER (RETRY WRAPPER & ERROR HANDLING)
# ==============================================================================

class AllRetriesFailedError(Exception):
    """Raised when all retry attempts fail[cite: 1]."""
    def __init__(self, attempts: int):
        self.attempts = attempts
        super().__init__(f"Operation failed after maximum limit of {self.attempts} attempts.")


def unreliable_call() -> str:
    """Simulates a flaky network function raising ConnectionError ~50% of the time."""
    if random.random() < 0.5:
        raise ConnectionError("503 Service Unavailable: Remote server dropped connection")
    return "API_RESPONSE_200_OK"


def safe_call(func, max_retries: int = 3):
    """
    Executes a callable safely, retrying up to max_retries specifically on ConnectionError[cite: 1].
    """
    for attempt in range(1, max_retries + 1):
        try:
            return func()
        except ConnectionError as err:
            logging.warning(f"Attempt {attempt}/{max_retries} failed: {err}")
            if attempt == max_retries:
                raise AllRetriesFailedError(attempts=max_retries) from err


# ==============================================================================
# SET A — PROBLEM 4: EMPLOYEE PAYROLL (CLASS VS INSTANCE ATTRIBUTES)
# ==============================================================================

class Employee:
    # Class attribute: Shared across all instances in memory[cite: 1]
    tax_rate: float = 0.20

    def __init__(self, name: str, base_salary: float):
        # Instance attributes: Unique per employee instance[cite: 1]
        self.name = name
        self.base_salary = base_salary

    def net_pay(self) -> float:
        # Refers to Employee.tax_rate so class updates propagate dynamically
        return self.base_salary * (1.0 - Employee.tax_rate)

    @classmethod
    def from_dict(cls, data: dict):
        """Alternative constructor initializing instance from a raw dictionary[cite: 1]."""
        return cls(name=data["name"], base_salary=data["base_salary"])


# ==============================================================================
# SET A — PROBLEM 5: LOGGING DECORATOR (HIGHER-ORDER FUNCTIONS & METADATA)
# ==============================================================================

def log_grades(func):
    """
    Decorator that logs input parameters, function return value, and timestamp[cite: 1].
    
    EXPLANATION OF FUNCTOOLS.WRAPS:
    Skipping @wraps(func) causes wrapper to overwrite the target function's 
    dunder attributes (e.g., __name__, __doc__) with 'wrapper'[cite: 1]. This breaks 
    debugging tools, inspection frameworks, and log tracebacks[cite: 1].
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = func(*args, **kwargs)
        print(f"[{timestamp}] called {func.__name__} with args={args} -> result={result}")
        return result
    return wrapper


@log_grades
def calculate_grade(score: float) -> str:
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"


# ==============================================================================
# SET B — PROBLEM 1: MESSY SURVEY CLEANUP (PANDAS DATA CLEANING)
# ==============================================================================

def clean_survey_data():
    raw_survey = [
        {"id": 1, "response": " Yes ", "age": 22.0},
        {"id": 2, "response": "no", "age": 35.0},
        {"id": 3, "response": "YES", "age": np.nan},
        {"id": 4, "response": "No", "age": 28.0},
        {"id": 5, "response": " yes", "age": 41.0},
        {"id": 6, "response": "NO ", "age": np.nan},
        {"id": 7, "response": "Yes", "age": 30.0},
        {"id": 7, "response": "Yes", "age": 30.0},  # Duplicate row
    ]

    df = pd.DataFrame(raw_survey)
    print("\n--- B1: Survey Summary BEFORE Cleaning ---")
    print(df.describe(include="all"))

    # 1. Strip whitespace and normalize text to lowercase
    df["response"] = df["response"].astype(str).str.strip().str.lower()
    
    # 2. Impute missing age values with column mean[cite: 4]
    df["age"] = df["age"].fillna(df["age"].mean())
    
    # 3. Deduplicate exact duplicate rows[cite: 4]
    df = df.drop_duplicates().reset_index(drop=True)

    print("\n--- B1: Survey Summary AFTER Cleaning ---")
    print(df.describe(include="all"))
    return df


# ==============================================================================
# SET B — PROBLEM 2: VECTORIZED GRADING CURVE (NUMPY BROADCASTING)
# ==============================================================================

def apply_vectorized_curve():
    scores = np.array([62, 78, 95, 88, 40, 99, 71])
    
    # Vectorized curve: adds 5 points using scalar broadcasting, capped at 100 via np.clip[cite: 4]
    curved = np.clip(scores + 5, a_min=None, a_max=100)
    
    """
    EXPLANATION OF VECTORIZATION PERFORMANCE:
    Vectorized NumPy operations execute operations over contiguous memory blocks in compiled 
    C code[cite: 4]. Python loops incur massive per-element overhead (dynamic type checking, 
    pointer chasing, and interpreter loop execution)[cite: 4]. Vectorization avoids this, 
    running orders of magnitude faster on large arrays[cite: 4].
    """
    print(f"\n--- B2: Vectorized Grading Curve ---")
    print(f"Original Scores: {scores}")
    print(f"Curved Scores:   {curved}")
    return curved


# ==============================================================================
# SET B — PROBLEM 3: NEAREST NEIGHBOR BY HAND (COSINE SIMILARITY)
# ==============================================================================

def find_nearest_customer():
    # Customer features: [recency_days, frequency_purchases, monetary_spend]
    existing_customers = np.array([
        [5, 20, 500],   # Customer 0
        [45, 2, 40],    # Customer 1
        [3, 18, 480],   # Customer 2
        [120, 1, 15]    # Customer 3
    ])
    new_customer = np.array([[4, 19, 490]])

    # Calculate Cosine Similarity between 2D array shapes[cite: 4]
    sim_scores = cosine_similarity(existing_customers, new_customer).flatten()

    # Sort indices high to low
    sorted_indices = np.argsort(sim_scores)[::-1]

    print("\n--- B3: Customer Cosine Similarity ---")
    for idx in sorted_indices:
        print(f"Customer {idx}: Similarity Score = {sim_scores[idx]:.4f}")
    
    print(f"Closest match is Customer {sorted_indices[0]}")


# ==============================================================================
# SET B — PROBLEM 4: SPAM FILTER CONFUSION MATRIX (EVALUATION METRICS)
# ==============================================================================

def evaluate_spam_filter():
    expected_labels  = ["spam", "ham", "spam", "spam", "ham", "ham", "spam", "ham", "spam", "ham"]
    predicted_labels = ["spam", "ham", "spam", "ham",  "ham", "spam", "spam", "ham", "spam", "ham"]
    
    labels = ["ham", "spam"]
    cm = confusion_matrix(expected_labels, predicted_labels, labels=labels)
    precision = precision_score(expected_labels, predicted_labels, pos_label="spam")
    recall = recall_score(expected_labels, predicted_labels, pos_label="spam")
    f1 = f1_score(expected_labels, predicted_labels, pos_label="spam")

    print("\n--- B4: Spam Filter Metrics ---")
    print(f"Confusion Matrix (rows=actual, cols=pred):\n{cm}")
    print(f"Precision (Spam): {precision:.2f}")
    print(f"Recall (Spam):    {recall:.2f}")
    print(f"F1-Score (Spam):  {f1:.2f}")

    """
    PLAIN-LANGUAGE ERROR ANALYSIS:
    In a spam filter context, a False Positive (FP) occurs when a legitimate email (ham) is 
    incorrectly labeled as spam and sent to the junk folder. A False Negative (FN) occurs 
    when an actual spam email slips into the user's main inbox. 
    
    Product Decision Strategy:
    In production, you prioritize minimizing False Positives (maximizing Precision). A user 
    missing a critical work email or job offer because it was misclassified into spam is far 
    more damaging than a user seeing an occasional piece of junk email in their inbox.
    """


# ==============================================================================
# SET B — PROBLEM 5: TOKEN BUDGET ESTIMATOR (HEURISTIC RETRIEVAL SANITY CHECK)
# ==============================================================================

def estimate_token_budget(chunks: list[str], max_context: int = 8000, reserved_for_output: int = 1000) -> int:
    """
    Estimates context window token usage using the heuristic ~4 chars per token[cite: 4].
    Raises ValueError if total tokens exceed available prompt capacity[cite: 1, 4].
    """
    available_budget = max_context - reserved_for_output
    total_tokens = sum(len(chunk) // 4 for chunk in chunks)

    if total_tokens > available_budget:
        excess = total_tokens - available_budget
        raise ValueError(
            f"Token budget exceeded! Required: {total_tokens} tokens. "
            f"Available limit: {available_budget} tokens. Exceeded by: {excess} tokens."
        )
    
    return total_tokens


# ==============================================================================
# DEMONSTRATION SUITE
# ==============================================================================

if __name__ == "__main__":
    print("================================================================================")
    print("RUNNING EXAM PRACTICE DEMONSTRATIONS")
    print("================================================================================\n")

    # --- A1 Demo ---
    print("--- A1: Library Tracker ---")
    book = Book("Hands-On Machine Learning", "978-1492032649")
    user = Member("Alice")
    print(book)
    user.borrow(book)
    print(book)
    
    # Failed borrow attempt catching custom exception
    try:
        user2 = Member("Bob")
        user2.borrow(book)
    except BookUnavailableError as e:
        print(f"[Caught Exception Successfully] {e}")
    
    user.return_book(book)
    print(book)

    # --- A2 Demo ---
    print("\n--- A2: Polymorphic Shape Total Area ---")
    shapes: list[Shape] = [Circle(3.0), Rectangle(4.0, 5.0), Triangle(3.0, 4.0, 5.0)]
    print(f"Total Area across all shapes: {total_area(shapes):.2f}")
    
    try:
        Rectangle(-2.0, 5.0)
    except ValueError as e:
        print(f"[Caught Validation Error Successfully] {e}")

    # --- A3 Demo ---
    print("\n--- A3: Retry API Caller ---")
    try:
        res = safe_call(unreliable_call, max_retries=3)
        print(f"API Safe Call Succeeded: {res}")
    except AllRetriesFailedError as e:
        print(f"API Safe Call Failed Completely: {e}")

    # --- A4 Demo ---
    print("\n--- A4: Employee Class Attributes ---")
    emp1 = Employee("John", 50000.0)
    emp2 = Employee.from_dict({"name": "Jane", "base_salary": 80000.0})
    
    print(f"Default Tax Rate: {Employee.tax_rate}")
    print(f"Emp1 Net Pay: ${emp1.net_pay():,.2f} | Emp2 Net Pay: ${emp2.net_pay():,.2f}")
    
    # Update Class Attribute globally
    Employee.tax_rate = 0.30
    print(f"Updated Tax Rate: {Employee.tax_rate}")
    print(f"Emp1 Net Pay: ${emp1.net_pay():,.2f} | Emp2 Net Pay: ${emp2.net_pay():,.2f}")

    # --- A5 Demo ---
    print("\n--- A5: Logging Decorator ---")
    score_result = calculate_grade(85.5)

    # --- B1 Demo ---
    clean_survey_data()

    # --- B2 Demo ---
    apply_vectorized_curve()

    # --- B3 Demo ---
    find_nearest_customer()

    # --- B4 Demo ---
    evaluate_spam_filter()

    # --- B5 Demo ---
    print("\n--- B5: Token Budget Estimator ---")
    sample_chunks = ["Detailed document chunk about RAG systems." * 20 for _ in range(5)]
    
    # Under budget pass
    tokens = estimate_token_budget(sample_chunks, max_context=8000, reserved_for_output=1000)
    print(f"Test 1 (Normal Batch): Total Tokens = {tokens} (Passed Budget Check)")

    # Over budget failure
    large_chunks = ["Massive context text chunk filling context window." * 200 for _ in range(10)]
    try:
        estimate_token_budget(large_chunks, max_context=8000, reserved_for_output=1000)
    except ValueError as e:
        print(f"Test 2 (Over Budget): [Caught Budget Exception] {e}")
