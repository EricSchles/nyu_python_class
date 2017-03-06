def mergesort(A):
    if len(A) <= 1:
        return A
    else:
        mid = len(A)//2
        return merge(mergesort(A[:mid]),mergesort(A[mid:]))

def merge(left,right):
    left_p,right_p = 0,0
    merged = []
    while left_p < len(left) and right_p < len(right):
        if left[left_p] < right[right_p]:
            merged.append(left[left_p])
            left_p += 1
        else:
            merged.append(right[right_p])
            right_p += 1
    while left_p < len(left):
        merged.append(left[left_p])
        left_p += 1
    while right_p < len(right):
        merged.append(right[right_p])
        right_p += 1
    return merged
