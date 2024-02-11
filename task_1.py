def caching_fibonacci():
    cache = {}
    
    def fibonacci(n): # Створення функції, яка заповнює кеш числами Фібоначчі
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
            return cache[n]
    
    def get_cache(): # Створення функції, яка буде повертати кеш, щоб він був доступний для перегляду 
        return cache

    return fibonacci, get_cache
    
fib, cache = caching_fibonacci()

print(fib(10))
print(cache())

print(fib(15))
print(cache())

print(fib(7)) 
print(cache())

print(fib(12)) 
print(cache())

print(fib(20)) 
print(cache())
