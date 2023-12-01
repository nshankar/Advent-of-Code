import java.io.File;  // Import the File class
//import java.util.ArrayList;
import java.util.Scanner;


public class P1 {
	public static void main(String []args) throws Exception{
		File data = new File("input.txt");
		Scanner reader = new Scanner(data);
		int score = 0;
		int prev = Integer.valueOf(reader.nextLine());
		while (reader.hasNextLine()) {
			int curr = Integer.valueOf(reader.nextLine());
			if (curr > prev) {
				score++;
			}
			prev = curr;
		}
		System.out.println(score);
	}
}