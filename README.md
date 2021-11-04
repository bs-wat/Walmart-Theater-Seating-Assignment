## Walmart-Theater-Seating-Assignment

### Assumptions:
 1. Customers can enter the seat from both the left and right sides to avoid crossing other groups as necessary.
 2. Customers prefer seats that are higher up and farther away from the screen.
 3. Customers will not want to be separated from their group and will always be in the same row as their group.
 4. Rows that are occupied will be separated from other occupied rows by one row at all times. Ex: If row 4 is occupied, rows 3 and 5 will be empty.

### Algorithm:
 1. Parse through the request file and store in a dictionary / hashmap for access when processing requests.
 2. For each request, find the appropriate seating based on the current arrangement and append the seating to the output file.
  a. Starting from the farthest / highest row of seats, check if the row can accomodate the requested seats and a three seat buffer. If not, jump two rows down and repeat as necessary.
  b. If the row is empty, allocate the seats to fulfill starting from the left.
  c. Else, traverse the row until there are three seats past the last occupied seat.
  d. Allocate these seats to the request starting from the seat right of the 3 seat buffer.
 3. Print / return the complete path for the output file.

### Instructions:
 Execute in command line with the format: "python movie_theater_seating.py {input file path} {output file name}"
 Ex: python movie_theater_seating.py C:\\Users\\Brandon\\Desktop\\Walmart\ Coding\ Assignment\\input.txt output.txt

 Output file name can be the file name or the complete path.
