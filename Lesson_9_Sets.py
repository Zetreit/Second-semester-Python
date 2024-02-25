# Задание №1
def count_unique_numbers(N, numbers):
    unique_numbers = set(numbers)
    return len(unique_numbers)

# Задание №2
def count_common_numbers(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_numbers = set1.intersection(set2)
    return len(common_numbers)

# Задание №3
def check_numbers(sequence):
    seen = set()
    for num in sequence:
        if num in seen:
            print("YES")
        else:
            print("NO")
            seen.add(num)

# Ввод данных и вызов функций
if __name__ == "__main__":
    # Задание №1
    N = int(input())
    numbers = list(map(int, input().split()))
    result1 = count_unique_numbers(N, numbers)
    print(result1)
    
    # Задание №2
    list1 = [int(input()) for _ in range(int(input()))]
    list2 = [int(input()) for _ in range(int(input()))]
    result2 = count_common_numbers(list1, list2)
    print(result2)
    
    # Задание №3
    sequence = list(map(int, input().split()))
    check_numbers(sequence)
