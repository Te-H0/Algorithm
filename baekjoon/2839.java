package baekjoon;

import java.io.*;
class Solution  {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw;
        int n;
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            bw = new BufferedWriter(new OutputStreamWriter(System.out));
            n = Integer.parseInt(br.readLine()); //배달해야하는 무게가 총 몇 kg
        }
        int answer = 0;
        while(n>0){
            if(n % 5  == 0){ //5로 나누어지면
                answer += n/5;
                break;
            }else { //만약 아니라면 3KG이거나 봉지에 담지 나눠담지 못하는 것.
                n -= 3;
                answer++;
            }
            if(n < 0){
                answer = -1;
            }
        }
        bw.write(answer + "");
        bw.flush();
        bw.close();

    }
}
