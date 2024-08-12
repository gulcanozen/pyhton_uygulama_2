import math
# 2D uzaydaki noktaları temsil eden liste
points = [(1, 2), (4, 6), (7, 1), (2, 8)]

# İki nokta arasındaki Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)*2 + (y2 - y1)*2)

# Mesafeleri saklayacağımız liste
distances = []

# Nokta çiftleri arasındaki mesafeleri hesaplama
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafe
min_distance = min(distances)

# Minimum mesafe yazdır
print(f"Minimum mesafe: {min_distance}")