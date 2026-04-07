class task2 {
    public static void is_prime(int n) {
        if (n <= 1) {
            System.out.println(n + " is not a prime number.");
            return;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                System.out.println(n + " is not a prime number.");
                return;
            }
        }
        System.out.println(n + " is a prime number.");
    }
    public static void main(String[] args) {
        is_prime(17);
        is_prime(20);
    }
}