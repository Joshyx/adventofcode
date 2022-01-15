using System;
using System.IO;

class Program {
  	public static void Main(string[] args) {
    	string[] input = File.ReadAllLines("adventofcode.txt");
    
    	string gamma = "";
    	string epsilon = "";

    	for(int i = 0; i < input[0].Length; i++) {
      		int timesCounted0 = 0;
      		int timesCounted1 = 0;

      		foreach(string bite in input) {
        		char bit = bite[i];

        		if(bit == '0') {
          			timesCounted0++;
        		} else if(bit == '1') {
          			timesCounted1++;
        		}
      		}

      		if(timesCounted0 > timesCounted1) {
        		gamma += 0;
        		epsilon += 1;
      		} else {
        		gamma += 1;
        		epsilon += 0;
      		}
    	 }

		   Console.WriteLine(Convert.ToInt32(gamma, 2) * Convert.ToInt32(epsilon, 2));
  	}
}
