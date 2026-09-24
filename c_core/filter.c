#include <stdio.h>

// Moving Average Filter in C for signal noise reduction
void apply_moving_average(float input[], float output[], int size, int window) {
    for (int i = 0; i < size; i++) {
        float sum = 0.0;
        int count = 0;
        for (int j = 0; j < window; j++) {
            if (i - j >= 0) {
                sum += input[i - j];
                count++;
            }
        }
        output[i] = sum / count;
    }
}
