
public class Gugudan_array {
	public static int[] calculate(int times) {
		int[] result = new int[9];
		for(int i=0; i < result.length; i++) {
			result[i] = times * (i + 1);
		}
		return result;
	}
	
	public static void print(int[] result) {
		for(int i=0; i < result.length; i++) {
			System.out.println(result[i]);
		}
	}
	
	public static void main(String[] args) {
		int[] result = calculate(3);
		print(result);

		
//		for(int i=0; i < result.length; i++) {
//			System.out.println(result[i]);
//		}
//				
//		int[] result = new int[9];
//		for(int i=0; i < result.length; i++) {
//			result[i] = 2 * (i + 1);
//		}
//		
//		for(int i=0; i < result.length; i++) {
//			System.out.println(result[i]);
//		}
//		
//		int[] times3 = new int[9];
//		for(int i=0; i < times3.length; i++) {
//			times3[i] = 3 * (i + 1);
//		}
//		
//		for(int i=0; i < times3.length; i++) {
//			System.out.println(times3[i]);
//		}
		
	}
}
