scum(1,1):-!.
scum(N,_):- \+integer(N); N < 1, !, write("Invalid input"), nl, fail.
scum(N, Sum):- N1 is N - 1, scum(N1, RestSum), Sum is RestSum + N.


sumDigits(0, 0):-!.
sumDigits(N,_):- \+integer(N); N < 0, !, write("Invalid input"), nl, fail.
sumDigits(Num, Sum):-Digit is Num mod 10, Rest is Num // 10, sumDigits(Rest, RestSum), Sum is RestSum + Digit.

split(N,_):- \+integer(N); N < 0, !, write("Invalid input"), nl, fail.
split(N, [N]):-integer(N), N >= 0, N < 10,!.
split(N, Res):-Digit is N mod 10, Rest is N // 10, split(Rest, RestRes), append(RestRes, [Digit], Res).

create(List, _):- \+is_list(List), !, write("Invalid input"), nl, fail.
create([N], N):- integer(N), N >= 0, N < 10, !.
create([Head|Rest], N):- \+integer(Head); Head < 0, !, write("Invalid input"), nl, fail.
create([Head|Rest], N):- create(Rest, RestN), N is RestN * 10 + Head.

reverseNum(N, Rev):- split(N, Digits), create(Digits, Rev).