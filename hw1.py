"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data


# Part 1: vowel_count
def vowel_count(text: str) -> int:
    # TODO: Purpose: counts the vowels in a string of text
    # TODO: Input(s): string
    # TODO: Output: int
    count = 0
    for letter in text.lower():
        if character in "aeiou":
            count += 1

    return count


# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: finds nested lists containing two elements
    # TODO: Input(s): list of lists
    # TODO: Output: list of lists
    result = []
    for item in items:
        if len(item) == 2:
            result.append(item)
    return result


# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: puts pairs of ints in non ascending order
    # TODO: Input(s): a list of lists
    # TODO: Output: a list of lists
    result = []
    for item in items:
        if len(item) == 2:
            if item[0] > item [1]
                result.append(item[1])
                result.append(item[0])
            else:
                result.append(item[0])
                result.append(item[1])
        else:
            result.append(item)
    return result

# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # TODO: Purpose: adds two prices together
    # TODO: Input(s): two price objects
    # TODO: Output: price object
    total_cents = first.cents + second.cents
    total_dollars = first.dollars + second.dollars

    total_dollars += total_cents // 100
    total_cents = total_cents % 100

    return data.Price(total_dollars, total_cents)



# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # TODO: Purpose: calculates area of a rectangle
    # TODO: Input(s): rectangle object
    # TODO: Output: float
    w = rectangle.bottom_right.x - rectangle.top_left.x
    l = rectangle.top_left.y = rectangle.bottom_right.y 
    return w * l


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # TODO: Purpose: lists books written by an author
    # TODO: Input(s): a string and a list
    # TODO: Output: a list
    result = []
    for book in books:
        if author in book.authors:
            result.append(book)
    return result


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # TODO: Purpose: finds smallest circle enclosing a rectangle
    # TODO: Input(s): rectangle object
    # TODO: Output: circle object
    center_x = (rectangle.top_left.x + rectangle.bottom_right.x) / 2
    center_y = (rectangle.top_left.y + rectangle.bottom_right.y) / 2

    center = data.Point(center_x, center_y)

    dx = rectangle.bottom_right.x - center_x
    dy = rectangle.bottom_right.y - center_y

    radius = (dx ** 2 + dy ** 2) ** 0.5

    return data.Circle(center, radius)


# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # TODO: Purpose: finds employees being paid below average wage
    # TODO: Input(s): listt
    # TODO: Output: list
    if len(employees) == 0:
        return []
    
    total = 0
    for emp in employees:
        total += emp.pay_rate
    
    avg = total/len(employees)

    result = []
    for employ in employees:
        if employ.pay_rate < average:
            result.append(employee.name)
    return result
    
    
