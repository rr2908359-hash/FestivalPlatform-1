import java.util.Scanner;

public class HangmanGame {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // List of words to guess
        String[] words = {"java", "programming", "hangman", "developer", "computer", "keyboard", "galgotia"};

        // Pick a random word
        String word = words[(int) (Math.random()]()
