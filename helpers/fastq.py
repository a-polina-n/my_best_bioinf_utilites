def calc_gc(seq: str) -> float:
    """
    Counts the GC content of a given sequence string.

    Args:
        seq (str): a nucleic acid sequence string.

    Returns:
        float: GC count (percent).
    """
    gc_count = sum(1 for c in seq.upper() if c in "GC")
    return (gc_count / len(seq)) * 100


def calc_mean_quality(qual_str: str) -> float:
    """
    Counts the mean quality of a read.

    Args:
        qual_str (str): a string of phed33 quality scores per each nucleotide.

    Returns:
        float: mean quality for a sequence.
    """
    return sum(ord(c) - 33 for c in qual_str) / len(qual_str)


def in_gc_bounds(gc: float, 
              bounds: float | tuple[float, float]) -> bool:
    """
    Checks if the given sequence string contains allowed GC count.

    Args:
    - gc (float): a nucleic acid string GC value.
    - bounds (tuple | float): a tuple with lower and upper GC boundaries, or a float upper boundary.

    Returns:
        bool
    """
    if isinstance(bounds, (int, float)):
        return gc <= bounds
    elif isinstance(bounds, tuple):
        low, high = bounds
        return low <= gc <= high


def in_len_bounds(length: int, 
              bounds: float | tuple[float, float]) -> bool:
    """
    Checks if the given sequence string is of an allowed GC length.

    Args:
    - length (int): a nucleic acid string length value.
    - bounds (tuple | int): a tuple with lower and upper length boundaries, or an integer lower boundary.

    Returns:
        bool
    """
    if isinstance(bounds, (int, float)):
        return length <= bounds
    elif isinstance(bounds, tuple):
        low, high = bounds
        return low <= length <= high


