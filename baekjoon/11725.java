package baekjoon;

import java.io.*;  
import java.util.*;  

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  
        int n = Integer.parseInt(br.readLine());  

        int[] parent = new int[n+1];
        boolean[] check = new boolean[n+1];
        ArrayList<Integer>[] graph = new ArrayList[n+1];
        for(int i=1;i<=n;i++){
            graph[i] = new ArrayList<>();
        }

        StringTokenizer st;  
        for (int i = 1; i < n; i++) {  
            st = new StringTokenizer(br.readLine());  
            int a = Integer.parseInt(st.nextToken());  
            int b = Integer.parseInt(st.nextToken());  
            graph[a].add(b);  
            graph[b].add(a);  
        }  
    }
}
