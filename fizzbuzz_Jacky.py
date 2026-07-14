# Step 1: Keep asking until user enters a valid number
while True:
    number = int(input("Enter a maximum number: "))

    if number < 1:
        print("Error: Please enter a number greater than 0.")
    else:
        break  # Valid number, exit loop

# Step 2: Create counters
fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

# Step 3: Loop from 1 to the number
for i in range(1, number + 1):

    # Check for FizzBuzz
    if i % 3 == 0 and i % 5 == 0:
        print(i, "- FizzBuzz")
        fizzbuzz_count += 1

    # Check for Fizz
    elif i % 3 == 0:
        print(i, "- Fizz")
        fizz_count += 1

    # Check for Buzz
    elif i % 5 == 0:
        print(i, "- Buzz")
        buzz_count += 1

    # Print number if no match
    else:
        print(i)

# Step 4: Print summary
print("\nSummary:")
print("Fizz count:", fizz_count)
print("Buzz count:", buzz_count)
print("FizzBuzz count:", fizzbuzz_count)