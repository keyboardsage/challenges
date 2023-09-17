bool isValid(char * s){
    const size_t S_SIZE = strlen(s);
    char* stack = (char*)malloc((S_SIZE+1) * sizeof(char));
    size_t top = 0;

    for (int i = 0; i < S_SIZE; i ++) {
        if (top == 0) { // empty stack so far, just add the character
            stack[top] = s[i];
            top++;
        } else if ( // encountered a companion bracket, just remove the opening bracket character
            (stack[top-1] == '(' && s[i] == ')') ||
            (stack[top-1] == '[' && s[i] == ']') ||
            (stack[top-1] == '{' && s[i] == '}')) top--;
        else if (stack[top-1] == '(' && (s[i] == ']' || s[i] == '}')) return false; // wrong closing bracket, fail
        else if (stack[top-1] == '[' && (s[i] == ')' || s[i] == '}')) return false;
        else if (stack[top-1] == '{' && (s[i] == ')' || s[i] == ']')) return false;
        else { // otherwise we are just accumulating opening brackets
            stack[top] = s[i];
            top++;
        }
    }

    if (top != 0) return false; // we were given too many opening brackets without companions, fail

    return true;
}