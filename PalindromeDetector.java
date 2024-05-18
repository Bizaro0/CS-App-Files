import java.util.Scanner;
public class PalindromeDetector 
{
	  static String response;
	  static String newResponse;

// Challenge - keep asking for palindrome until user enters the correct one

// 				MAIN METHOD

 public static void main(String [] args) 
 {
	Scanner reader = new Scanner(System.in);

	// PALINDROME DETECTOR

	response = "";
	newResponse = "";
	boolean loop = true;
	do {
		System.out.print("Enter word: ");
		String response = reader.nextLine();
		response = response.toLowerCase(); // Cases such as "Mom" would now pass since entire string is now lowercase.
		System.out.println();
		
		String [] palindrome = response.split(""); // Utiizes split to divide string up and adds it to newResponse.
		 newResponse = "";

		for (int i = palindrome.length-1; i >= 0; i--) 	
		{
			newResponse+=palindrome[i];
		}

		System.out.println();

		if (response.equals(newResponse)) 
		{
			System.out.println("This word is a palindrome");
			loop = false;
		}
			
		else 
		{
		  System.out.println("This word is not a palindrome");
		}
		System.out.println();

	    } while (loop);
	
	}
}










