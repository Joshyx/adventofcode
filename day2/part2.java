import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		List<String> inputValues = getInputValues();
		
		int horizontalPos = 0;
		int depth = 0;
		int aim = 0;
		
		for(String command : inputValues) {
			String commandName = command.split(" ")[0];
			int commandParameter = Integer.parseInt(command.split(" ")[1]);
			
			switch(commandName) {
				case "forward":
					horizontalPos += commandParameter;
					depth += aim * commandParameter;
					break;
				case "down":
					aim += commandParameter;
					break;
				case "up":
					aim -= commandParameter;
					break;
			}
		}
		
		System.out.println(horizontalPos * depth);
	}
	
	private static List<String> getInputValues() {
		Path path = Paths.get("C:\\Users\\Joschi\\Desktop\\adventofcode.txt");
		try {
			return Files.readAllLines(path);
		} catch (IOException e) {
			e.printStackTrace();
			System.exit(1);
			return null;
		}
	}
}
