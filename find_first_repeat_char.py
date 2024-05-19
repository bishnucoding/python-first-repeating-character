def find_first_repead_char(input):
    map = {}
    for a_char in input:
        if a_char in map:
            return a_char
        else:
            map[a_char] = True
    return '/0'        

input = 'bishnubrata'
input = 'gogetit'
result = find_first_repead_char(input)
print(result)

# Time complexity: O(n). Because insert and lookup of map is constant time.
# Space complexity: O(n). Because additional map is used, which can store upto n elements.