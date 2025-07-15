# Performance - Quick Notes

- Use built-in functions and libraries — they are optimized  
- Avoid unnecessary computations inside loops  
- Use list/dict/set comprehensions for faster iteration  
- Use generators for large datasets to save memory  
- Avoid global variables when possible  
- Profile your code to find bottlenecks (cProfile, timeit)  
- Cache results of expensive functions with functools.lru_cache
