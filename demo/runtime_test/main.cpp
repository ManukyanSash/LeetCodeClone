#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>


int main(int argc, char** argv) {
    std::string lang = argv[1];
    std::string command = "";
    std::string firstArg;
    std::string secondArg;
    int result;
    std::fstream finalRes("runtime_test/final.txt");
    std::vector<int> params;// fun
    if ( lang == "python") {
        command += "python3 runtime_test/file.py";
    } else if (lang == "C++") {
        command += "runtime_test/file";
    } else if (lang == "Java") {
        command += "java runtime_test.file";    
    } else if (lang == "JS") {
        command += "node runtime_test/file.js";
    }
    std::ifstream infile("runtime_test/file_test.txt");
    std::string line;

    while (std::getline(infile, line)) {
        std::stringstream ss(line);
        std::vector<int> numbers;
        int number;
        while (ss >> number) {
            numbers.push_back(number);
            if (ss.peek() == ',') {
                ss.ignore();
            }
        }
        if (numbers.size() != 3) {
            std::cout << "Error: expected three numbers, but found " << numbers.size() << std::endl;
            continue;
        }
        firstArg = std::to_string(numbers[0]);
        secondArg = std::to_string(numbers[1]);
        system((command + " " + firstArg + " " +secondArg).c_str());
        std::ifstream output("runtime_test/output.txt", std::ios::in);
        output >> result;
        
        if (result != numbers[2]) {
            std::cout << "The test case for Args: " << numbers[0] << " and " << numbers[1] << "is not correct\nexpected: " << numbers[2];
            return 0;
        }
        numbers.clear();
    }
    
    std::cout << "true";
}
