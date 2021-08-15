"""
Simple use case of prefect for the evening of python coding
"""

from prefect import task, Flow
import sys
import time
import datetime


# uncomment next line to make this into a task
# @task
def is_prime(number):
    """determine if a number is prime"""
    # 0 and 1 are not considered prime numbers although 1 is positive and divisible by 1 and itself
    prime = number > 1
    for possible_divider in range(2, number):
        if number % possible_divider == 0:
            prime = False
    return prime


# uncomment next line to make this into a task
# @task
def only_primes(is_prime_vector):
    """reduce the vector to show only primes """
    only_prime_vector = [number for (number, is_prime_number) in enumerate(is_prime_vector) if is_prime_number]
    return only_prime_vector


# uncomment next line to make this into a task
# @task
def break_down_to_primes(number, only_prime_vector):
    """break down each number only to primes and return the computation string"""
    left_to_divide = number
    dividers_list = []
    while left_to_divide > 1:
        possible_divider_index = 0
        while possible_divider_index < len(only_prime_vector):
            possible_divider = only_prime_vector[possible_divider_index]
            if left_to_divide % possible_divider == 0:
                left_to_divide = left_to_divide / possible_divider
                dividers_list.append(str(possible_divider))
            else:
                possible_divider_index += 1
    # if more than one divider found, write down the formula -
    # otherwise its a prime, if no divider found - write not prime
    if len(dividers_list) == 0:
        output_string = ('%i is not prime ' % number)
    elif len(dividers_list) == 1:
        output_string = ('%i is prime ' % number)
    else:
        output_string = ('%i = ' % number) + '*'.join(dividers_list)
    return output_string


# noinspection PyArgumentList
@task(max_retries=10, retry_delay=datetime.timedelta(seconds=3))
def output_to_file(output_strings, start_number, lines_per_file):
    """outputs the string nicely to a file with an extension defined"""
    filename = 'prefect_demo%i.txt' % start_number
    file = open(filename, 'w')
    for output_string in output_strings[start_number: (start_number + lines_per_file)]:
        file.write(output_string + '\n')
    file.close()
    return filename


# main code
if __name__ == '__main__':
    # default max number and max number of lines per file
    max_number = 20000
    max_lines_per_file = 5000
    if len(sys.argv) > 1:
        # extract user defined max number
        max_number = int(sys.argv[1])
    if len(sys.argv) > 2:
        max_lines_per_file = int(sys.argv[2])

    start_time = time.time()
    # find a vector of prime numbers
    with Flow("prime flow") as flow:
        glob_is_prime_vector = [is_prime(i) for i in range(max_number)]
        print('Primes computed by %f sec' % (time.time() - start_time))
        # collect only the prime numbers
        only_prime_numbers = only_primes(glob_is_prime_vector)
        print('Only primes extracted by %f sec' % (time.time() - start_time))
        # break down the numbers to only primes
        divider_strings = [break_down_to_primes(i, only_prime_numbers) for i in range(max_number)]
        print('Divisions computed by %f sec' % (time.time() - start_time))
        files_created = [output_to_file(divider_strings, file_number, max_lines_per_file)
                         for file_number in range(0, max_number, max_lines_per_file)]
        print('save to files by %f sec' % (time.time() - start_time))
    flow.run()
    print('All Done after %f sec' % (time.time() - start_time))
