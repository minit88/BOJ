package baekjoon_java.DP;
import java.util.*;
import java.io.*;

public class BOJ1577 {
    static long[][] dp;
    static int[][][] road;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        dp = new long[m + 1][n + 1];
        road = new int[m + 1][n + 1][2];

        dp[0][0] += 1;

        int construction_road = Integer.parseInt(br.readLine());

        // 공사 중인 도로 체크
        for (int i = 0; i < construction_road; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            // 세로 방향의 도로가 공사일 경우
            if (a-c == 0){

                // 두 y 좌표 비교
                if(b>d){
                    road[b][a][1]=-1;
                }
                else{
                    road[d][c][1]=-1;
                }
            }

            // 가로 방향의 도로가 공사일 경우
            else if (b-d == 0){

                // 두 x 좌표 비교
                if(a>c){
                    road[b][a][0]=-1;
                }
                else{
                    road[d][c][0]=-1;
                }

            }
        }

        // dp 계산
        for (int i = 0; i < m + 1; i++) {
            for (int j = 0; j < n + 1; j++) {

                // 가로에서 오는 거 먼저 검증
                if (j - 1 >= 0) {
                    if (road[i][j][0] == 0 ) {
                        dp[i][j] += dp[i][j - 1];
                    }
                }

                // 세로에서 오는 거 검증
                if (i - 1 >= 0) {
                    if (road[i][j][1] == 0) {
                        dp[i][j] += dp[i - 1][j];
                    }
                }
            }
        }
        if(n==0 && m==0){
            dp[0][0]-=1;
        }
        System.out.println(dp[m][n]);

    }
}