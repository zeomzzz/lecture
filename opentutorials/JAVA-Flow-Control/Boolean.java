public class BooleanApp {

	public static void main(String[] args) {
		
		System.out.println("One"); // 문자열 (String)
		System.out.println(1); // 정수 (Int)
		
		System.out.println(true); // Boolean
		System.out.println(false); // Boolean
		
		String foo = "Hello world";
		//String true = "Hello world"; // reserved word
		// true, false 는 boolean 값이어서 변수로 지정할 수 없음
		
		System.out.println(foo.contains("world")); // true
		System.out.println(foo.contains("egoing")); //false
		
	}

}
