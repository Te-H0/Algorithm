package programmers;
import java.util.*;
class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int height = triangle.length;
        
        int[][] tree = new int[height][];
        for(int i = 0 ; i<height;i++){
            tree[i] = new int[i+1];
        }
        tree[0][0] = triangle[0][0];
        
        // System.out.println(height);
        
        for(int i = 0 ; i< height -1 ; i++){
            for(int j = 0 ; j < i+1; j++){
                if (tree[i+1][j] < triangle[i+1][j] + tree[i][j]){
                    tree[i+1][j] = triangle[i+1][j] + tree[i][j];
                }
                if (tree[i+1][j+1] < triangle[i+1][j+1] + tree[i][j]){
                    tree[i+1][j+1] = triangle[i+1][j+1] + tree[i][j];
                }
                
            }
        }
        answer = Arrays.stream(tree[tree.length-1]).max().getAsInt();
        // System.out.println(Arrays.deepToString(tree));
        return answer;
    }
}