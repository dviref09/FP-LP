scum(1,1):-!.
scum(N,_):- (\+integer(N); N < 1), !, write("Invalid input"), nl, fail.
scum(N, Sum):- N1 is N - 1, scum(N1, RestSum), Sum is RestSum + N.


sumDigits(0, 0):-!.
sumDigits(N,_):- (\+integer(N); N < 0), !, write("Invalid input"), nl, fail.
sumDigits(Num, Sum):-Digit is Num mod 10, Rest is Num // 10, sumDigits(Rest, RestSum), Sum is RestSum + Digit.

split(N,_):- (\+integer(N); N < 0), !, write("Invalid input"), nl, fail.
split(N, [N]):-integer(N), N >= 0, N < 10,!.
split(N, Res):-Digit is N mod 10, Rest is N // 10, split(Rest, RestRes), append(RestRes, [Digit], Res).

create(List, _):- \+is_list(List), !, write("Invalid input"), nl, fail.
create([N], N):- integer(N), N >= 0, N < 10, !.
create([Head|_], _):- (\+integer(Head); Head < 0), !, write("Invalid input"), nl, fail.
create([Head|Rest], N):- create(Rest, RestN), N is RestN * 10 + Head.

reverseNum(N, Rev):- split(N, Digits), create(Digits, Rev).

subset([], []):-!.
subset(_, L):- \+is_list(L), !, write("Invalid input"), nl, fail.
subset([H|T1], [H|T2]):- subset(T1, T2).
subset(S, [_|T]):- subset(S, T).

listsum([], 0):-!.
listsum([H|_], Sum):- (\+integer(H); \+integer(Sum)), !, write("Invalid input"), nl, fail.
listsum([H|T], Sum):- listsum(T, RestSum), Sum is RestSum + H.
subsum(L, Sum, SubSet):- subset(SubSet, L), (listsum(SubSet, Sum) -> true ; !, fail).

intersection([], _, []):-!.
intersection(_, [], []):-!.
intersection(L1, L2, _):- (\+is_list(L1); \+is_list(L2)), !, write("Invalid input"), nl, fail.
intersection([H|T], L2, L):-member(H, L2), !, intersection(T, L2, Rest), L = [H|Rest].
intersection([_|T], L2, L):- intersection(T, L2, L). 

minus([], _, []):-!.
minus(L1, L2, _):- (\+is_list(L1); \+is_list(L2)), !, write("Invalid input"), nl, fail.
minus([H|T], L2, L):- \+member(H, L2), !, minus(T, L2, Rest), L = [H|Rest].
minus([_|T], L2, L):- minus(T, L2, L).