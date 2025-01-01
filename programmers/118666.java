package programmers;

class Solution {
    public int[] sol2(String s){
        int t = -1;
        int q1 = -1;
        int q2 = -1;
        if(s.contains("R")){
            t = 0;
            if(s.charAt(0) =='R'){
                q1 = 0;
                q2 = 1;
            }
            else{
                q1 = 1;
                q2 = 0;
            }
        }
        else if(s.contains("C")){
            t = 1;
            if(s.charAt(0) =='C'){
                q1 = 0;
                q2 = 1;
            }
            else{
                q1 = 1;
                q2 = 0;
            }
        }
        else if(s.contains("J")){
            t = 2;
            if(s.charAt(0) =='J'){
                q1 = 0;
                q2 = 1;
            }
            else{
                q1 = 1;
                q2 = 0;
            }
        }
        else if(s.contains("A")){
            t = 3;
            if(s.charAt(0) =='A'){
                q1 = 0;
                q2 = 1;
            }
            else{
                q1 = 1;
                q2 = 0;
            }
        }

    
        return new int[]{t,q1,q2};
    }

    public String solution(String[] survey, int[] choices) {
        String answer = "";
        int[][] score = new int[4][2];
        char[][] type = {{'R', 'T'}, {'C', 'F'}, {'J', 'M'}, {'A', 'N'}};

        for(int i = 0; i<survey.length;i++){
            int[] tmp = sol2(survey[i]);
            int t = tmp[0];
            int q1 = tmp[1];
            int q2 = tmp[2];
            int point = 4- choices[i];

            if(point > 0){
                score[t][q1] += point;
            }
            else if(point <0){
                score[t][q2] -= point;
            }
        }

        for(int i = 0; i<score.length;i++){
            if(score[i][0] >= score[i][1]){
                answer += type[i][0];
            }
            else{
                answer += type[i][1];
            }
        }
        return answer;
    }
    public static void main(String[] args) {
        Solution sol = new Solution(); // Solution 객체 생성
        String[] survey = {"AN", "CF", "MJ", "RT", "NA"};
        int[] choices = {5, 3, 2, 7, 5};
        
        System.out.println(sol.solution(survey, choices)); // 메서드 호출
    }
}