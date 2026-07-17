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

kuku_tail([], []):-!. % green cut
kuku_tail(L1,L2):-kuku_tail_helper(L1,[],L2).
kuku_tail_helper([],Acc,Acc):-!. % green cut
kuku_tail_helper([H|T],Acc,L):- H2 is 2 * H, kuku_tail_helper(T, [[H, H2]|Acc], L).

kuku_non_tail([], []):-!. % green cut
kuku_non_tail([H|T], L2):- H2 is 2 * H, kuku_non_tail(T, L3), append(L3, [[H, H2]], L2). 

kuku_nested([],[]):-!. % green cut
kuku_nested([H|T], L2):- is_list(H), !, kuku_nested(T, L3), kuku_nested(H, L4), append(L3, [L4], L2). % red cut 
kuku_nested([H|T], L2):- H2 is 2 * H, kuku_nested(T, L3), append(L3, [[H, H2]], L2). 

flattenList_non_tail([],[]):-!. % green cut
flattenList_non_tail([H|T], L):- is_list(H), !, flattenList_non_tail(H, L2), flattenList_non_tail(T, L3), append(L2, L3, L). % red cut
flattenList_non_tail([H|T], L):- flattenList_non_tail(T, L3), append([H], L3, L).

flattenList_tail([],[]):-!. % green cut
flattenList_tail(L1, L2):-flattenList_tail_helper(L1, [], L2).
flattenList_tail_helper([], Acc, Acc):-!. % green cut
flattenList_tail_helper([H|T], Acc, L):-is_list(H), !, flattenList_tail(H, L2), append(Acc, L2, NewAcc), flattenList_tail_helper(T, NewAcc, L). % red cut
flattenList_tail_helper([H|T], Acc, L):- append(Acc, [H], NewAcc), flattenList_tail_helper(T, NewAcc, L).

deepReverse([], []):-!. % green cut
deepReverse([H|T], R):- is_list(H), !, deepReverse(H, R1), deepReverse(T, R2), append(R2, [R1], R). % red cut
deepReverse([H|T], R):- deepReverse(T, R1), append(R1, [H], R).