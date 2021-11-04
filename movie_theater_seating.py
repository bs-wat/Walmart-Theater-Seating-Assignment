# Walmart Summer 2022 Internship - Movie Theater Seating Assignment
# Candidate: Brandon Wat

import sys
import os

def parse_requests(request_file, hashmap):

    with open(request_file, "r") as customer_requests:
        lines = customer_requests.readlines()

        # fill the dictionary to with request_id as key and number of seats as values
        for i in range(len(lines)):
            entry = lines[i].split(" ")
            
            request_id = entry[0]
            num_seats = entry[1]

            hashmap[request_id] = int(num_seats)

def find_seats(num_seats, curr_seating, row_map):
    chosen_seats = []
    chosen_row = 0

    # check if there is a free row
    for i in range(len(curr_seating) - 1, -1, -2):
        curr_row = curr_seating[i]

        enough_seats_for_buffer = curr_row.count(0) >= (num_seats + 3)

        # check if the row has enough seats for 3 seat buffer
        if enough_seats_for_buffer:

            if curr_row[0] == 0: # empty row -> assign checking open seats
                for n in range(num_seats):
                    curr_row[n] = 1
                    chosen_seats.append(n)
                    chosen_row = i

            # otherwise -> need to check for open seats
            open_seats = 0

            for j in range(len(curr_row)):
                if curr_row[j] == 0 and open_seats < 3: # mark seats as buffer seats until adequate buffer achieved
                    curr_row[j] = -1
                    open_seats += 1
                elif open_seats == 3: # adequate buffer -> assign the seats
                    for m in range(num_seats):
                        curr_row[j + m] = 1
                        chosen_seats.append(j + m)
                        chosen_row = i
                
                if len(chosen_seats) == num_seats:
                    break
        else: 
            continue # check next row(as in the one that is a row apart)

        if len(chosen_seats) == num_seats:
            break

    # return the seats chosen
    return [ ( row_map[chosen_row] + str(x + 1) ) for x in chosen_seats ]

def driver(request_file, output_name):
    # 0 = open seat , 1 = occupied, -1 = buffer
    theater = [ [0 for _ in range(20)] for _ in range(10) ]

    # map the row number to letters
    rows = {}
    r = "ABCDEFGHIJ"

    for i in range(10):
        rows[i] = r[i]

    output = open(output_name, "a")

    # parse the request_file for easy access in dictionary
    requests = dict()
    parse_requests(request_file, requests)

    # for each request find seats based on current arrangement
    for req_id in requests:
        seats = find_seats(requests[req_id], theater, rows)

        assigned_seats = ",".join(seats)
        result = f"{req_id} {assigned_seats}" 
        
        output.write(result + "\n")

    # close output file
    output.close()

    # form the complete path of the output file and print/return it
    complete_path = os.path.abspath(output_name)
    print(complete_path)

    return complete_path

if __name__ == "__main__":
    driver(sys.argv[1],sys.argv[2])