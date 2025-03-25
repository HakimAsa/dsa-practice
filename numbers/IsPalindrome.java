// Solution for is_palindrome (integer) in java
package numbers;

public class IsPalindrome {
    public static void main(String[] args) {
        int x = 121;
        System.out.println("testing");
        System.out.println(isPalindrome(x)); // true
        System.out.println(isPalindrome(-x)); // false
        System.out.println(isPalindrome(10)); // false
    }

    public static boolean isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int rev = 0;
        int temp = x;
        while (temp != 0) {
            int digit = temp % 10;
            rev = rev * 10 + digit;
            temp /= 10;
        }

        return x == rev;
    }
}