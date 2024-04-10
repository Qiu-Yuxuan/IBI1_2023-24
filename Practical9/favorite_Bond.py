def favorite(birth_year):
    """
    input: the year when the person was born
    code: add 18 to the birth year and choose the favorite Bond
    output: a string vairble stating the individual's Bond actor
    """
    year_18=birth_year+18
    if year_18>=1973 and year_18<=1986:
        favorite_Bond="Roger Moore"
    elif year_18>=1987 and year_18<=1994:
        favorite_Bond="Timothy Dalton"
    elif year_18>=1995 and year_18<=2005:
        favorite_Bond="Pierce Brosnan"
    elif year_18>=2006 and year_18<=2021:
        favorite_Bond="Daniel Craig"
    else:
        favorite_Bond="can't judge"
    return(favorite_Bond)
#example
print(favorite(1986))
