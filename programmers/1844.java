package programmers;

import java.util.*;  

class Solution {
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0}; // 위, 아래, 왼, 오
    static boolean[][] visit;
    static int n;
    static int m; 
    
    public int solution(int[][] maps) {
        int answer = 0;
        n = maps.length;
        m = maps[0].length;
        visit = new boolean[n][m];
        answer = bfs(maps);
        return answer;
    }
    
    public int bfs(int[][] maps){
        Queue<int[]> qu = new LinkedList<>();
        
        qu.add(new int[]{0,0,1});
        visit[0][0] = true;
        
        while(!qu.isEmpty()){
            int temp[] = qu.poll();
            int x = temp[0];
            int y = temp[1];
            int count = temp[2];
            
            if(x == n-1 && y == m-1){
                return count;
            }
            
            for(int i =0; i<4;i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if((0 <= nx && nx < n) && (0 <= ny && ny < m ) && maps[nx][ny] == 1 &&!visit[nx][ny]){
                    qu.add(new int[] {nx, ny, count + 1});
                    visit[nx][ny] = true;
                }
            }
        }
        return -1;
    }
}
