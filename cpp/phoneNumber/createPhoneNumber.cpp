#include <iostream>
#include <string>


std::string createPhoneNumber(const int arr [10]);

int main() {
    int array[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
    std:: cout << createPhoneNumber(array);

    return 0;
}

std::string createPhoneNumber(const int arr [10]) {
    std::string total = "(";
    total += std::to_string(arr[0]) + std::to_string(arr[1]) + std::to_string(arr[2]) + ") " + std::to_string(arr[3])
                                    + std::to_string(arr[4]) + std::to_string(arr[5]) + " - " + std::to_string(arr[6]) + std::to_string(arr[7])
                                    + std::to_string(arr[8]) + std::to_string(arr[9]);
    return total;
}




/*
    Assert::That(createPhoneNumber(arr{1, 2, 3, 4, 5, 6, 7, 8, 9, 0}), Equals("(123) 456-7890"));
        Assert::That(createPhoneNumber(arr{1, 1, 1, 1, 1, 1, 1, 1, 1, 1}), Equals("(111) 111-1111"));
        Assert::That(createPhoneNumber(arr{1, 2, 3, 4, 5, 6, 8, 8, 0, 0}), Equals("(123) 456-8800"));
        Assert::That(createPhoneNumber(arr{0, 2, 3, 0, 5, 6, 0, 8, 9, 0}), Equals("(023) 056-0890"));
        Assert::That(createPhoneNumber(arr{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}), Equals("(000) 000-0000"));

*/
