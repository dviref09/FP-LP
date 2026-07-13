% the recursive call is tail because the last operation in the predicate is the recursive call
last_three([X, Y, Z], X, Y, Z):-!. % green cut
last_three([_ | T], X, Y, Z):-last_three(T, X, Y, Z).

% question 2
% tail recursive
union_tail_helper([], Acc, Acc):-!. %green cut
union_tail_helper([H|T], Acc, L3):-member(H, Acc), !, union_tail_helper(T, Acc, L3). % red cut
union_tail_helper([H|T], Acc, L3):-union_tail_helper(T, [H|Acc], L3).
union_tail(L1, L2, L3):-list_to_set(L1, L4), list_to_set(L2, L5), union_tail_helper(L4, L5, L3).
% non_tail recursive
union_non_tail([], L1, L2):- list_to_set(L1, L3), L2 = L3, !. %green cut
union_non_tail([H|T], L1, L2):-(member(H, L1) ; member(H, T)), !, union_non_tail(T, L1, L2). % red cut
union_non_tail([H|T], L1, [H|L2]):-union_non_tail(T, L1, L2).