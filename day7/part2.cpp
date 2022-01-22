#include <iostream>
#include <fstream>
#include <list>

std::list<int> split(std::string line, std::string delimiter) {
	std::list<int> values;
	std::string token;
	int start = 0;
    int end = line.find(delimiter);
    while (end != -1) {
        values.push_back(std::stoi(line.substr(start, end - start)));
        start = end + delimiter.size();
        end = line.find(delimiter, start);
    }
    values.push_back(std::stoi(line.substr(start, end - start)));

	return values;
}

std::list<int> getLines() {
	std::string line;
	std::ifstream file("input.txt");
	getline(file, line);
	file.close();

	return split(line, ",");
}

int neededFuel(std::list<int> values, int average) {
	int neededFuel = 0;
	for(int value : values) {
		int fuel = 0;
		for(int i = 1; i <= abs(value - average); i++) {
			fuel += i;
		}
		neededFuel += fuel;
	}
	return neededFuel;
}

int main() {
	std::list<int> values = getLines();
	values.sort();
	std::list<int> fuelValues;

	for(int i = values.front(); i <= values.back(); i++) {
		fuelValues.push_back(neededFuel(values, i));
	}
	fuelValues.sort();
	std::cout << fuelValues.front() << std::endl;
};
