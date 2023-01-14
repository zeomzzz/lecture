
public class LogicalOperatorApp {

	public static void main(String[] args) {
		
		System.out.println(1 == 1); // true
		
		// 논리연산자 : 연산자 양쪽이 모두 true 또는 false 여야 함
		// AND : &&
		System.out.println(true && true); // true
		System.out.println(true && false); // false
		System.out.println(false && true); // false
		System.out.println(false && false); // false
		
		// OR : ||
		System.out.println(true || true); // true
		System.out.println(true || false); // true
		System.out.println(false || true); // true
		System.out.println(false || false); // false
		
		// not
		System.out.println(!true); // false
		System.out.println(!false); // true
		
	}

}
