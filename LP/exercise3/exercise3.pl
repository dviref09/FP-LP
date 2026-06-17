scum_helper(1,1):-!.
scum_helper(N,Res):-N1 is N - 1, scum_helper(N1, Res1), Res is Res1 + N.
scum(N,Res):-(integer(N), N > 1) -> scum_helper(N,Res); (write("invalid input"), nl, fail).

sumDigits(0, 0):-!.
sumDigits(Num, Sum):-integer(Num), Num >= 0, Digit is Num mod 10, Rest is Num // 10, sumDigits(Rest, RestSum), Sum is RestSum + Digit.

split(N, [N]):-integer(N), N >= 0, N < 10,!.
split(N, Res):-(integer(N), N > 0, Digit is N mod 10, Rest is N // 10, split(Rest, RestRes), append(RestRes, [Digit], Res)).