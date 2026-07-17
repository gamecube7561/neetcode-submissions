class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int[][] res = new int[k][2];
        int resSize = 0;

        if (k >= points.length) {
            return points;
        }

        PriorityQueue<int[]> pq =
            new PriorityQueue<>((p2, p1)
                                    -> Double.compare(Math.sqrt((p1[0] * p1[0]) + (p1[1] * p1[1])),
                                        Math.sqrt((p2[0] * p2[0]) + (p2[1] * p2[1]))));

        for (int[] p : points) {
            if (pq.size() < k) {
                pq.add(p);
            } else {
                int p1 = pq.peek()[0];
                int p2 = pq.peek()[1];

                if (Math.sqrt((p1 * p1) + (p2 * p2)) > Math.sqrt((p[0] * p[0]) + (p[1] * p[1]))) {
                    pq.poll();
                    pq.add(p);
                }
            }
        }

        while (pq.size() > 0) {
            res[resSize] = pq.poll();
            resSize++;
        }

        return res;
    }
}
