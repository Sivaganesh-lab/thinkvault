import hashlib

def hash_idea(idea: str) -> str:
    """Takes a string idea and returns its SHA-256 hash"""
    return hashlib.sha256(idea.encode()).hexdigest()
