import java.io.File;  // Import the File class
import java.util.ArrayList;
import java.util.Scanner;


public class P2 {
	public static void main(String[] args) throws Exception{
		ArrayList<Integer> data = new ArrayList<>();
		File file = new File("input.txt");
		Scanner reader = new Scanner(file);
		int score = 0;
		int step = 3;
		while (reader.hasNextLine()) {
			data.add(Integer.parseInt(reader.nextLine()));
		}
		for (int i=0; i<data.size()-step; ++i) {
			if (data.get(i) < data.get(i+step)) {
				++score;
			}
		}
		System.out.println(score);
	}
}