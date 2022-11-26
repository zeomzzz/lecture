
public class StringApp {

	public static void main(String[] args) {
		
		System.out.println("Hello World"); // String (문자열 : 문자가 모여 있음)
		System.out.println('H'); // Character (문자 : 한 글자)
		System.out.println("H"); // String
		
		System.out.println("Hello "
				+ "World"); // 줄바꿈 되지 않음
		
		// \n : new line (n)
		System.out.println("Hello \nWorld");
		
		// escape : \ 이용하여 뒤의 역할 있는 문자를 일시적으로 도망시킴
		System.out.println("Hello \"World\""); //Hello "World"

	}

}
