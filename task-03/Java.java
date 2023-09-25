package kunal;
import java.util.*;

public class Java {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n;

        System.out.println("Enter a number : ");
        n = in.nextInt();

        System.out.println("The Prime numbers up to " + n + " are :- ");
        for (int i = 2; i <= n; i++) {
            int c = 0;
            for (int j = 1; j <= i; j++) {
                if (i % j == 0) {
                    c++;
                }
            }
            if (c == 2) {
                System.out.println(i);
            }
        }
    }
}
