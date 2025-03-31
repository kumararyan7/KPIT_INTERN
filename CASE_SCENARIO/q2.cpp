// Write the following function that returns the sum of the float s pointed to by the first n
// pointers in the array p : float sum(float* p[], int n)

float sum(float* p[], int n) {
    float total = 0.0;
    for (int i = 0; i < n; i++) {
        total += *p[i];
    }
    return total;
}


float sun (float)