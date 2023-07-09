/* 
 *  This code uses ansi
 *  escape codes
 *  
 *  source https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
 *  
 */

#define RESET          "\033[0m"
/*
 *  effects
 */
#define BOLD           "\033[1m"
#define DIM            "\033[2m"
#define ITALIC         "\033[3m"
#define UNDERLINE      "\033[4m"
#define BLINK          "\033[5m"
#define REVERSE        "\033[7m"
#define INVISIBLE      "\033[8m"
#define DASHED         "\033[9m"
/*
 *  reset effects
 */
#define UN_BOLD        "\033[22m"
#define UN_DIM         "\033[22m"
#define UN_ITALIC      "\033[23m"
#define UN_UNDERLINE   "\033[24m"
#define UN_BLINK       "\033[25m"
#define UN_REVERSE     "\033[27m"
#define UN_INVISIBLE   "\033[28m"
#define UN_DASHED      "\033[29m"
/*
 *  foreground colors
 */
#define FG_BLACK       "\033[30m"
#define FG_RED         "\033[31m"
#define FG_GREEN       "\033[32m"
#define FG_yellow      "\033[33m"
#define FG_BLUE        "\033[34m"
#define FG_MAGENTA     "\033[35m"
#define FG_CYAN        "\033[36m"
#define FG_WHITE       "\033[37m"
#define FG_DEFAULT     "\033[38m"
/*
 *  background colors
 */
#define BG_BLACK       "\033[30m"
#define BG_RED         "\033[31m"
#define BG_GREEN       "\033[32m"
#define BG_yellow      "\033[33m"
#define BG_BLUE        "\033[34m"
#define BG_MAGENTA     "\033[35m"
#define BG_CYAN        "\033[36m"
#define BG_WHITE       "\033[37m"
#define BG_DEFAULT     "\033[38m"

#include <stdio.h>

#define RESET          "\033[0m"

/*
 *  effects
 */
#define BOLD           "\033[1m"
#define DIM            "\033[2m"
#define ITALIC         "\033[3m"
#define UNDERLINE      "\033[4m"
#define BLINK          "\033[5m"
#define REVERSE        "\033[7m"
#define INVISIBLE      "\033[8m"
#define DASHED         "\033[9m"

/*
 *  reset effects
 */
#define UN_BOLD        "\033[22m"
#define UN_DIM         "\033[22m"
#define UN_ITALIC      "\033[23m"
#define UN_UNDERLINE   "\033[24m"
#define UN_BLINK       "\033[25m"
#define UN_REVERSE     "\033[27m"
#define UN_INVISIBLE   "\033[28m"
#define UN_DASHED      "\033[29m"

/*
 *  foreground colors
 */
#define FG_BLACK       "\033[30m"
#define FG_RED         "\033[31m"
#define FG_GREEN       "\033[32m"
#define FG_YELLOW      "\033[33m"
#define FG_BLUE        "\033[34m"
#define FG_MAGENTA     "\033[35m"
#define FG_CYAN        "\033[36m"
#define FG_WHITE       "\033[37m"
#define FG_DEFAULT     "\033[38m"

/*
 *  background colors
 */
#define BG_BLACK       "\033[40m"
#define BG_RED         "\033[41m"
#define BG_GREEN       "\033[42m"
#define BG_YELLOW      "\033[43m"
#define BG_BLUE        "\033[44m"
#define BG_MAGENTA     "\033[45m"
#define BG_CYAN        "\033[46m"
#define BG_WHITE       "\033[47m"
#define BG_DEFAULT     "\033[49m"

const char* get_macro(int choice) {
    switch (choice) {
        case 1:
            return BOLD;
        case 2:
            return DIM;
        case 3:
            return ITALIC;
        case 4:
            return UNDERLINE;
        case 5:
            return BLINK;
        case 6:
            return REVERSE;
        case 7:
            return INVISIBLE;
        case 8:
            return DASHED;
        case 9:
            return UN_BOLD;
        case 10:
            return UN_DIM;
        case 11:
            return UN_ITALIC;
        case 12:
            return UN_UNDERLINE;
        case 13:
            return UN_BLINK;
        case 14:
            return UN_REVERSE;
        case 15:
            return UN_INVISIBLE;
        case 16:
            return UN_DASHED;
        case 17:
            return FG_BLACK;
        case 18:
            return FG_RED;
        case 19:
            return FG_GREEN;
        case 20:
            return FG_YELLOW;
        case 21:
            return FG_BLUE;
        case 22:
            return FG_MAGENTA;
        case 23:
            return FG_CYAN;
        case 24:
            return FG_WHITE;
        case 25:
            return FG_DEFAULT;
        case 26:
            return BG_BLACK;
        case 27:
            return BG_RED;
        case 28:
            return BG_GREEN;
        case 29:
            return BG_YELLOW;
        case 30:
            return BG_BLUE;
        case 31:
            return BG_MAGENTA;
        case 32:
            return BG_CYAN;
        case 33:
            return BG_WHITE;
        case 34:
            return BG_DEFAULT;
        default:
            return RESET;
    }
}

int main() {
    int choice;
    printf("Enter your choice:\n");
    printf("1. BOLD\n");
    printf("2. DIM\n");
    printf("3. ITALIC\n");
    printf("4. UNDERLINE\n");
    printf("5. BLINK\n");
    printf("6. REVERSE\n");
    printf("7. INVISIBLE\n");
    printf("8. DASHED\n");
    printf("9. UN_BOLD\n");
    printf("10. UN_DIM\n");
    printf("11. UN_ITALIC\n");
    printf("12. UN_UNDERLINE\n");
    printf("13. UN_BLINK\n");
    printf("14. UN_REVERSE\n");
    printf("15. UN_INVISIBLE\n");
    printf("16. UN_DASHED\n");
    printf("17. FG_BLACK\n");
    printf("18. FG_RED\n");
    printf("19. FG_GREEN\n");
    printf("20. FG_YELLOW\n");
    printf("21. FG_BLUE\n");
    printf("22. FG_MAGENTA\n");
    printf("23. FG_CYAN\n");
    printf("24. FG_WHITE\n");
    printf("25. FG_DEFAULT\n");
    printf("26. BG_BLACK\n");
    printf("27. BG_RED\n");
    printf("28. BG_GREEN\n");
    printf("29. BG_YELLOW\n");
    printf("30. BG_BLUE\n");
    printf("31. BG_MAGENTA\n");
    printf("32. BG_CYAN\n");
    printf("33. BG_WHITE\n");
    printf("34. BG_DEFAULT\n");
    printf("Enter your choice number: ");
    scanf("%d", &choice);
    const char* macro = get_macro(choice);
    printf("The selected macro is: %sExample text%s\n", macro, RESET);
    return 0;
}