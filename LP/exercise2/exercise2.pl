my_reverse([], R, R).
my_reverse([H|T], A, R):- my_reverse(T, [H|A], R).
my_reverse(L, R):- my_reverse(L, [], R).

my_prefix(S, L):- append(S, _, L).

my_member(X, [X|_]).
my_member(X, [_|T]):- my_member(X, T).

my_member2(X, L):- append(L1, L2, L), my_member(X, L1), my_member(X, L2).

my_palindrome(L):- my_reverse(L, L).

my_sorted([]).
my_sorted([_]).
my_sorted([X, Y|T]):- X =< Y, my_sorted([Y|T]).

my_insert(X, [], [X]).
my_insert(X, [H|T], [X, H|T]):- X =< H.
my_insert(X, [H|T1], [H|T2]):- H =< X, my_insert(X, T1, T2).