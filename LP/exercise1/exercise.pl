% in married the first argument is the husband and the second is the wife
father(X,Y):-parent(X,Y), male(X).
mother(X,Y):-parent(X,Y), female(X).
son(X,Y):-parent(Y,X), male(X).
daughter(X,Y):-parent(Y,X), female(X).
grandfather(X,Y):-father(X,Z), parent(Z,Y).
grandmother(X,Y):-mother(X,Z), parent(Z,Y).
grandson(X,Y):-son(X,Z), parent(Y,Z).
granddaughter(X,Y):-daughter(X,Z), parent(Y,Z).
sibling(X,Y):-parent(Z,X), parent(Z,Y), X\=Y.
% X is the first in the married paradict so he is for sure male
uncleNoBloodConn(X,Y):-parent(Z,Y), married(X,W), sibling(W, Z).
sonOfAunt(X,Y):-uncleNoBloodConn(Z,Y), son(X, Z).
% from the wife prespective
brotherInLaw(X,Y):-married(Z,Y), sibling(X,Z).
brotherInLaw(X,Y):-married(X,Z), sibling(Z,Y).
brotherInLaw(X,Y):-married(Z,Y), sibling(Z,W), married(X,W).
% from the husband prespective
brotherInLaw(X,Y):-married(Y,Z), sibling(X,Z).
brotherInLaw(X,Y):-married(X,Z), sibling(Z,Y).
brotherInLaw(X,Y):-married(Y,Z), sibling(Z,W), married(X,W).
niece(X,Y):-daughter(X,Z), sibling(Z,Y).
% helper paradict for second degree cousins
cousins(X,Y):-parent(Z,X), parent(W,Y), sibling(Z,W).
secondCousins(X,Y):-parent(Z,X), parent(W,Y), cousins(Z,W).
nieceOfGrandmother(X,Y):-grandmother(Z,X), niece(Y,Z).