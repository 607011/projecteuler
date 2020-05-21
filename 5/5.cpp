// http://projecteuler.net/index.php?section=problems&id=5
// Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>
	
#include <cstdio>


int main(int argc, char *argv[])
{
    static const int divisors[] = { 11, 13, 14, 15, 16, 17, 18, 19, 20, 0 };
	int x = 2;
	bool divisible = true;
	while (divisible) {
        for (int *p = (int*)divisors; *p != 0; ++p) {
			divisible &= (x % *p == 0);
			if (!divisible)
				break;
		}
		if (divisible)
			break;
		++x;
		divisible = true;
	}
	printf("%d\n", x);
	return 0;
}
