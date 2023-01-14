
public class ArrayApp {

	public static void main(String[] args) {
		// egoing, jinhuck, youbin
//		String users = "egoing, jinhuck, youbin";
		
		// 빈 깡통 배열 만들고, 배열에 값을 추가하기
		String[] users = new String[3];
		users[0] = "egoing";
		users[1] = "jinhuck";
		users[2] = "youbin";
		
		System.out.println(users[1]);
		System.out.println(users.length);
		
		// 배열 생성할 때 내용도 입력
		String[] scores = {10, 100, 100};

		System.out.println(scores[1]);
		System.out.println(scores.length);

	}

}
