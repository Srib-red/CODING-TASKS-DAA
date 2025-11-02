import math

# ---------- Helper function to compute Euclidean distance ----------
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


# ---------- Brute force for small sets ----------
def brute_force(points):
    min_dist = float('inf')
    pair = (None, None)
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return min_dist, pair


# ---------- Find minimum distance in strip ----------
def strip_closest(strip, d_min):
    min_dist = d_min
    pair = (None, None)

    # Sort strip by y-coordinate
    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            # Only check points within d_min in y
            if (strip[j][1] - strip[i][1]) < min_dist:
                d = distance(strip[i], strip[j])
                if d < min_dist:
                    min_dist = d
                    pair = (strip[i], strip[j])
            else:
                break
    return min_dist, pair


# ---------- Main Divide and Conquer function ----------
def closest_pair(points):
    n = len(points)
    if n <= 3:
        return brute_force(points)

    mid = n // 2
    mid_point = points[mid]

    # Divide into left and right halves
    dl, pair_left = closest_pair(points[:mid])
    dr, pair_right = closest_pair(points[mid:])

    # Find smaller distance
    if dl < dr:
        d_min = dl
        best_pair = pair_left
    else:
        d_min = dr
        best_pair = pair_right

    # Build the strip
    strip = [p for p in points if abs(p[0] - mid_point[0]) < d_min]

    # Find closest in strip
    ds, pair_strip = strip_closest(strip, d_min)
    if ds < d_min:
        return ds, pair_strip
    else:
        return d_min, best_pair


# ---------- Driver code ----------
if __name__ == "__main__":
    points = [(2, 3), (12, 30), (40, 50), (5, 1),(12, 10), (3, 4), (7, 2), (20, 25)]

    # Sort points by x-coordinate before starting
    points.sort(key=lambda p: p[0])

    min_dist, best_pair = closest_pair(points)
    print(f"Closest Pair: {best_pair}")
    print(f"Minimum Distance: {min_dist:.3f}")
