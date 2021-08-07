using System;

namespace fizzbuzz
{
    /*Write a program that prints the numbers from 1 to 100.

    But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".

    For numbers which are multiples of both three and five print "FizzBuzz".*/

    class Program
    {
        public static bool is_prime(int number)
        {
            bool is_a_prime = true;

            if (number > 3)
            {
                int half_of_number = number / 2;
                for (int i = 2; i <= half_of_number; i++)
                {
                    int remainder_of_number_divided_by_an_int = number % i;
                    if (remainder_of_number_divided_by_an_int == 0)
                    {
                        is_a_prime = false;
                        break;
                    }
                }
            }
            else if (number == 2 || number == 3)
                is_a_prime = true;
            else
                is_a_prime = false;
            return is_a_prime;
        }

        static void Main(string[] args)
        {
            for (int i = 1; i < 101; i++)
            {
                if (is_prime(i) == true)
                {
                    Console.WriteLine("prime");
                }
                else if (i % 3 == 0)
                {
                    if (i % 5 == 0)
                        Console.WriteLine("FizzBuzz");
                    else
                        Console.WriteLine("Fizz");
                }
                else if (i % 5 == 0)
                    Console.WriteLine("Buzz");
                else
                    Console.WriteLine(i);
            }
        }
    }
}
