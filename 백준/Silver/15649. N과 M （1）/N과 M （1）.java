import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] nums = new int[n];
        boolean[] used = new boolean[n];
        int[] output = new int[m];

        for (int i = 0; i < n; i++){
            nums[i] = i + 1;
        }
        permute(nums, output, used, 0, m);
        sc.close();
        
    }
    private static void permute(int[] nums, int[] output, boolean[] used, int depth, int m){
        if (depth == m){
            for (int i = 0; i < m; i++){
                System.out.print(output[i] + " ");
            }
            System.out.println();
            return;
        }
        for (int i = 0; i < nums.length; i++){
            if (!used[i]){
              used[i] = true;
                output[depth] = nums[i];
                permute(nums, output, used, depth + 1, m);
                used[i] = false;
            }
        }

    }
}