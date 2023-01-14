
public class AuthApp {

	public static void main(String[] args) {
		
		System.out.println(args[0]);
		
		String id = "egoing";
		String inputId = args[0]; // args[0] = egoing 저
		
		String pass = "1111";
		String inputPass = args[1];
		
		System.out.println("Hi.");
		
//		if(inputId.equals(id)) { // inputId == id 라고 작성하면 Who are you? 출
//			if(inputPass.equals(pass)) {
//				System.out.println("Master!");				
//			} else {
//				System.out.println("Wrong password!");
//			}
//		} else {
//			System.out.println("Who are you?");
//		}

		if(inputId.equals(id) && inputPass.equals(pass)) { // inputId == id 라고 작성하면 Who are you? 출
			System.out.println("Master!");				
		} else {
			System.out.println("Who are you?");
		}
		
	}

}
