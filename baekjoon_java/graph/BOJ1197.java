import java.util.*;
import java.io.*;

public class BOJ1197 {
    static int[] parent;
    static int result;

    static class Node implements Comparable<Node>{
        int A,B,val;

        Node(int A,int B,int val){
            this.A = A;
            this.B=B;
            this.val = val;
        }

        @Override
        public int compareTo(Node a){
            int val = a.val;
            if(this.val>val)
                return 1;
            else
                return -1;
        }
    }

    // 노드는 오름차순으로 연결
    static void unionParent(int x,int y){

        int x_parent = findParent(x);
        int y_parent = findParent(y);
        if (x_parent > y_parent){
            parent[x_parent]= y_parent;
        }
        else {
            parent[y_parent] = x_parent;
        }
    }

    // 현재 노드의 부모 검색
    static int findParent(int x){
        if (parent[x] != x){
            parent[x]= findParent(parent[x]);
        }
        return parent[x];
    }

    // ArrayList<Integer> parent = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());

        // 부모 배열 생성 및 초기화
        parent = new int[V+1];
        for (int i=0;i<V+1 ; i++){
            parent[i] = i;
        }

        // 간선 개수만큼 데이터 불러옴
        List<Node> l = new ArrayList<>();

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int val = Integer.parseInt(st.nextToken());

            l.add(new Node(A, B, val));
        }

        // 비용 순으로 정리
        Collections.sort(l);

        for (Node a : l){
            int A = a.A;
            int B = a.B;
            int val = a.val;

            if (findParent(A)!=findParent(B)){
                unionParent(A,B);
                result += val;
            }
        }

    System.out.println(result);
    for(int i = 0 ; i<V+1;i++){
        System.out.println(parent[i]);
    }
    }
}