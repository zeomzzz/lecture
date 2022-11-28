
public class Casting {

	public static void main(String[] args) {
		
		double a = 1.1;
		double b = 1; // int를 double에 담기 가능 : 손실이 없기 때문에 자동으로 casting
		double b2 = (double) 1; // 수동으로(명시적으로) casting
		
		System.out.println(b);
		
		
//		int c = 1.1;
		double d = 1.1;
		int e = (int) 1.1; // double을 강제로 int로 변경
		System.out.println(e); // 1.1(double) -> 1(int) : 손실 발생
		
		// 1 to String
		String f = Integer.toString(1); // int -> String casting
		System.out.println(f.getClass()); // data type 확인
		
		
	}

}
