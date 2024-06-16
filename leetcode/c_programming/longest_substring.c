int lengthOfLongestSubstring(char* s) {
    int i, end, start, max_len, current_len;
    int charIndex[128];

    i = end = start = max_len = current_len = 0;
    for (; i < 128; i++) {
        charIndex[i] = -1;
    }

    while (s[end] != '\0') {
        if (charIndex[s[end]] != -1 && charIndex[s[end]] >= start) {
            start = charIndex[s[end]] + 1;
        }
        charIndex[s[end]] = end;

        current_len = (end - start) + 1;
        if (current_len > max_len) {
            max_len = current_len;
        }
        end++;
    }

    return max_len;
}
