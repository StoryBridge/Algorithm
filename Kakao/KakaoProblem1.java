package kakao1;

public class Solution {
	public static void main(String[] args) {
		int input = 5;
		int[] arr1 = { 9, 20, 28, 18, 11 };
		int[] arr2 = { 30, 1, 21, 17, 28 };
		int[] result = new int[5];

		for (int i = 0; i < 5; i++) {
			result[i] = arr1[i] | arr2[i];
			char[] a = Integer.toBinaryString(result[i]).toCharArray();
			for(int j = 0 ; j<a.length; j++) {
				if (a[j] == '1') {
					System.out.print("#");
				} else if (a[j] == '0') {
					System.out.print(" ");
				}
			}
			System.out.print(", ");
		}

	}
}
