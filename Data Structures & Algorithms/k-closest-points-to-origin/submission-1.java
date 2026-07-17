class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int[][] res = new int[k][2];
        int resSize = 0;

        if (k >= points.length) {
            return points;
        }

        PriorityQueue<int[]> pq =
            new PriorityQueue<>((p1, p2)
                                    -> Double.compare(Math.sqrt((p1[0] * p1[0]) + (p1[1] * p1[1])),
                                        Math.sqrt((p2[0] * p2[0]) + (p2[1] * p2[1]))));

        for (int[] p : points) {
            pq.add(p);
        }

        while (k > 0) {
            res[resSize] = pq.poll();
            resSize++;
            k--;
        }

        return res;
    }
}
