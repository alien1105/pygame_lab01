"""Lab 01 public functions.

Implement the published contract without changing the function names or
parameters. Keep this module free of input(), print(), files, and UI code.
"""


def classify_score(score: int) -> str:
    """Return ``red``, ``amber``, or ``green`` for a score from 0 to 100."""
    if type(score) != int:
        raise TypeError
    if 0<= score <=59:
        return "red"
    elif 60<= score <=79:
        return "amber"
    elif 80<= score <=100:
        return "green"
    elif score < 0 or score > 100:
        raise ValueError 




def format_student_record(name: str, score: int) -> str:
    """Return ``<trimmed name> | <score> | <classification>``."""
    if type(name) != str:
        raise TypeError
    name = name.strip()
    if name == "":
        raise ValueError
    else:
        return f"{name} | {score} | {classify_score(score)}"

