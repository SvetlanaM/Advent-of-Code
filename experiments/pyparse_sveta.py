import pyparsing as pp

LPAREN, RPAREN, COLON, COMMA = map(pp.Suppress, "():,")


def convert_to_tuple(token_numbers):
    for number in token_numbers:
        return tuple(number)


def main(data: str):
    key = pp.Word(pp.alphas + ":_")
    number = pp.Word(pp.nums)
    number_tuple = pp.Group(number + COMMA + number) | number
    number_tuple = number_tuple.setParseAction(convert_to_tuple)
    s_expression = pp.Forward()
    s_expression << (
        key |
        number_tuple |
        pp.Group(LPAREN + (pp.ZeroOrMore(s_expression | pp.Suppress(COMMA))) + RPAREN)
    )

    s_expression_parsed = s_expression.parse_string(data)
    print(s_expression_parsed.as_list())


if __name__ == "__main__":
    # main(
    #     "(urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:1046880265))"
    # )
    # main(
    #     "(hiringContext:urn:li:ts_contract:454242226,hiringProject:urn:li:ts_hiring_project:(urn:li:ts_contract:454242226,1023782746),sourcingChannels:List(),candidateHiringStates:List(urn:li:ts_hiring_state:(urn:li:ts_contract:454242226,12771243472),urn:li:ts_hiring_state:(urn:li:ts_contract:454242226,12771237053),urn:li:ts_hiring_state:(urn:li:ts_contract:454242226,12771240858),urn:li:ts_hiring_state:(urn:li:ts_contract:454242226,12771238020)),candidates:List(urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:822788489),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:471749602),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:321738690),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:264380410),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:79594111),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:456103694),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:703614994),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:1000008365),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:853897833),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:759058262),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:886302767),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:355893023),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:836786118),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:354506061),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:1068418612),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:500083085),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:20695580),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:870075147),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:389225849),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:1025019805),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:724108945),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:709750789),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:573883196),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:456381588),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:363934506)))"  # noqa
    # )
    main(
        "(facetSelections:List((type:SOURCING_CHANNEL,valuesWithSelections:List()),(type:CANDIDATE_HIRING_STATE,valuesWithSelections:List((value:urn:li:ts_hiring_state:(urn:li:ts_contract:454254206,12771247229),selected:true,negated:false,required:false),(value:urn:li:ts_hiring_state:(urn:li:ts_contract:454254206,12771251051),selected:true,negated:false,required:false),(value:urn:li:ts_hiring_state:(urn:li:ts_contract:454254206,12771252348),selected:true,negated:false,required:false),(value:urn:li:ts_hiring_state:(urn:li:ts_contract:454254206,12771251050),selected:true,negated:false,required:false)))),capSearchSortBy:HIRING_CANDIDATE_LAST_UPDATED_DATE,hiringProjects:List((text:python,entity:urn:li:ts_hiring_project:(urn:li:ts_contract:454254206,1042246722))))"  # noqa
    )
