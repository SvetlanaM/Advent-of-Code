import pyparsing as pp
import urllib.parse

LPAREN, RPAREN, COLON, COMMA = map(pp.Suppress, "():,")


def decode_url(encoded_string: str) -> str:
    return urllib.parse.unquote(encoded_string)


"""
Goal: Transform data to JSON format
"""


# TODO: Merge list to the keys and add support for List with one (
def main(data: str) -> None:
    s_expression = pp.Forward()
    key = pp.Word(pp.alphanums + "_")
    key_with_colon = key + pp.Literal(":")
    number = pp.Word(pp.nums)
    number_tuple = number + COMMA + number | number
    special_value = pp.Combine(pp.ZeroOrMore(key_with_colon |
                                             pp.Literal("(") |
                                             pp.Literal(",") |
                                             number
                                             ) + pp.Literal(")"))

    value = special_value | s_expression | key | number_tuple
    value_with_selections = pp.Dict(pp.Group(key + COLON + value), COMMA)
    grammar = pp.Group(pp.Suppress(LPAREN) + pp.delimitedList(value_with_selections) + pp.Suppress(RPAREN))

    s_expression << (
            pp.Optional("List") + pp.Suppress("(") +
            pp.ZeroOrMore(pp.delimitedList(grammar)) +
            pp.Suppress(")")
    )

    print(grammar.parse_string(decode_url(data))[0])


if __name__ == "__main__":
    # main(
    #  "(urn:li:ts_contract:(urn:li:ts_contract:454242226,urn:li:ts_contract:1046880265))"
    # )
    # main(
    #     "(hiringContext:urn%3Ali%3Ats_contract%3A454242226,hiringProject:urn%3Ali%3Ats_hiring_project%3A%28urn%3Ali%3Ats_contract%3A454242226%2C1023782746%29,sourcingChannels:List(),candidateHiringStates:List(urn%3Ali%3Ats_hiring_state%3A%28urn%3Ali%3Ats_contract%3A454242226%2C12771243472%29,urn%3Ali%3Ats_hiring_state%3A%28urn%3Ali%3Ats_contract%3A454242226%2C12771237053%29,urn%3Ali%3Ats_hiring_state%3A%28urn%3Ali%3Ats_contract%3A454242226%2C12771240858%29,urn%3Ali%3Ats_hiring_state%3A%28urn%3Ali%3Ats_contract%3A454242226%2C12771238020%29),candidates:List(urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A463246085%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A261196946%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A248055030%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A217601564%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A180218842%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A18872159%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A832047721%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A724060579%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A907594609%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A586354084%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A451478538%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A571990312%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A1090469418%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A641525032%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A637458246%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A615553942%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A1034218181%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A388729411%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A978154619%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A140778485%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A515074761%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A506398555%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A940844324%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A699222892%29,urn%3Ali%3Ats_hiring_candidate%3A%28urn%3Ali%3Ats_contract%3A454242226%2Curn%3Ali%3Ats_hire_identity%3A861726787%29))"
    # )
    main(
        "(facetSelections:List((type:SOURCING_CHANNEL,valuesWithSelections:List()),(type:CANDIDATE_HIRING_STATE,valuesWithSelections:List((value:urn%3Ali%3Ats_hiring_state%3A%28urn%3Ali%3Ats_contract%3A454254206%2C12771247229%29,selected:true,selected:false,required:false),(value:urn%3Ali%3Ats_hiring_state%3A%28urn%3Ali%3Ats_contract%3A454254206%2C12771251051%29,selected:true,negated:false,required:false),(value:urn%3Ali%3Ats_hiring_state%3A%28urn%3Ali%3Ats_contract%3A454254206%2C12771252348%29,selected:true,negated:false,required:false),(value:urn%3Ali%3Ats_hiring_state%3A%28urn%3Ali%3Ats_contract%3A454254206%2C12771251050%29,selected:true,negated:false,required:false)))),capSearchSortBy:HIRING_CANDIDATE_LAST_UPDATED_DATE,hiringProjects:List((text:python,entity:urn%3Ali%3Ats_hiring_project%3A%28urn%3Ali%3Ats_contract%3A454254206%2C1042246722%29)))"
    )
