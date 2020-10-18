import functools

class IDIterator:
    """
    A class used to generate a valid id number.
    """

    def __init__(self, id_n):
        """Initial Values of the IDIterator class.
        :param id_n: a person id number.
        :type id_n: str.
        :returns: nothing, just assigning initial values.
        :rtype: None.
        """
        self.id_n = id_n

    def __iter__(self):
        """:returns: the iterator (IDIterator) instance
        :rtype: IDIterator.
        """
        return self

    def __next__(self):
        """checking if the next id number (after the user input) is valid throw check_id_valid function.
        :raise: StopIteration: raises an StopIteration Exception.
        :raise: ValueError: raises an Value Exception.
        :raise: SyntaxError: raises an Syntax Exception.
        :raise: IndexError: raises an Index Exception.
        :returns: The next valid id number.
        :rtype: int.
        """
        try:
            self.id_n = int(self.id_n) + 1  # Turning a string into an int & calling for the next id number.
            if len(str(self.id_n)) == 9:  # Checking if id number is exceeding the length of 9 figures.
                while self.id_n <= 999999999:  # Checking if the id number is exceeding the limit of 999999999.
                    for n in range(self.id_n, 1000000000):
                        if not check_id_valid(n):  # If the id number is no valid don't return anything but keep going.
                            self.id_n += 1
                            n += 1
                        else:
                            self.id_n += 1
                            n += 1
                            return self.id_n - 1  # Return the valid id number.
                else:
                    raise StopIteration
            else:
                raise IndexError

        except StopIteration:
            raise StopIteration
        except ValueError:
            raise ValueError
        except SyntaxError:
            raise SyntaxError
        except IndexError:
            raise IndexError


def check_id_valid(id_number):
    """checking if the id number is valid.
    :returns: The next valid id number.
    """
    num = str(id_number)
    list_num = []
    check_list_num = []
    for i in num:
        list_num.append(int(i))
    for digit in range(len(list_num)):
        if (digit + 1) % 2 == 0:
            pow_by_2 = list_num[digit] * 2  # Powering up the number (in the place of digit) if digit is even.
            if pow_by_2 > 9:  # if the Power up number is bigger then 9, add the first figure with the second.
                num_gen = (int(i) for i in str(pow_by_2))
                new_num = next(num_gen) + next(num_gen)
                check_list_num.append(new_num)
            else:
                check_list_num.append(pow_by_2)
        else:
            check_list_num.append(list_num[digit])
    final_num = (check_list_num[n] for n in range(len(check_list_num)))
    final_gen = functools.reduce(lambda a, b: a + b, final_num)  # sum's up all the result's of final_num.
    if final_gen % 10 == 0:  # Checking if the sum (final_gen) divide by 10 without leftovers.
        return True
    else:
        return False


def id_generator(check_num):
    """checking if the next id number (after the user input) is valid throw check_id_valid function.
    :raise: StopIteration: raises an StopIteration Exception.
    :raise: ValueError: raises an Value Exception.
    :raise: SyntaxError: raises an Syntax Exception.
    :raise: IndexError: raises an Index Exception.
    :returns: The next valid id number.
    """
    try:
        if len(check_num) == 9:  # Checking if id number is exceeding the length of 9 figures.
            id_number = int(check_num)  # Turning a string into an int.
            for n_g in range(id_number + 1, 1000000000):
                if check_id_valid(n_g):
                    yield n_g
                elif n_g > 999999999: # Checking if the id number is exceeding the limit of 999999999.
                    raise StopIteration
                else:
                    n_g += 1
        else:
            raise IndexError

    except StopIteration:
        raise StopIteration
    except ValueError:
        raise ValueError
    except SyntaxError:
        raise SyntaxError
    except IndexError:
        raise IndexError


def main():
    """Calling to the IDIterator & id_generator and print 10 valid id numbers.
    :raise: StopIteration: raises an StopIteration Exception.
    :raise: ValueError: raises an Value Exception.
    :raise: SyntaxError: raises an Syntax Exception.
    :raise: IndexError: raises an Index Exception.
    :returns: 10 valid id numbers.
    """
    try:
        user_input = input("Pls enter your ID:")

        print("\n")
        print("IDIterator result: \n")
        iter_id_number = IDIterator(user_input)
        for i in range(0, 10):  # Gives only 10 valid id numbers.
            print(next(iter_id_number))

        print("\n")
        print("generator result: \n")
        gen_id_number = id_generator(user_input)
        for i in range(0, 10):  # gives only 10 valid id numbers.
            print(next(gen_id_number))

    except ValueError:
        print("\nValueError: ID number as invalid character!")
    except SyntaxError:
        print("\nSyntaxError: ID number is not valid!")
    except StopIteration:
        print("\nStopIteration Error: end of the line bud..")
    except IndexError:
        print("\nIndexError: ID number is NOT in the right length!")


main()
