import pyparsing as pp
import urllib.parse


LPAREN, RPAREN, COLON, COMMA = map(pp.Suppress, "():,")


def decode_url(encoded_string: str) -> str:
    return urllib.parse.unquote(encoded_string)


def main(data: str):
    s_expression = pp.Forward()
    key = pp.Word(pp.alphanums + "_")
    number = pp.Word(pp.nums)
    key_with_colon = key + pp.Literal(":")
    number_tuple = number + COMMA + number | number
    special_value = pp.Combine(pp.ZeroOrMore(key_with_colon |
                                             pp.Literal("(") |
                                             pp.Literal(",") |
                                             number
                                             ) + pp.Literal(")"))

    value = special_value | s_expression | key | number_tuple
    valueWithSelections = pp.Dict(pp.Group(key + COLON + value), COMMA).setParseAction()
    grammar = pp.Group(pp.Suppress(LPAREN) + pp.delimitedList(valueWithSelections) + \
              pp.Suppress(RPAREN))

    s_expression << (
        pp.Suppress("List") + pp.Suppress("(") +
        pp.ZeroOrMore(pp.delimitedList(grammar)) +
        pp.Suppress(")")
    )

    print(grammar.parse_string(decode_url(data))[0])


if __name__ == "__main__":
    # main(
    #  "(urn:li:ts_contract:(urn:li:ts_contract:454242226,urn:li:ts_contract:1046880265))"
    # )
    main(
        "(hiringContext:urn:li:ts_contract:454242226,hiringProject:urn:li:ts_hiring_project:(urn:li:ts_contract:454242226,1023782746),sourcingChannels:List(),candidateHiringStates:List((urn:li:ts_hiring_state:(urn:li:ts_contract:454242226,12771243472),urn:li:ts_hiring_state:(urn:li:ts_contract:454242226,12771237053),urn:li:ts_hiring_state:(urn:li:ts_contract:454242226,12771240858),urn:li:ts_hiring_state:(urn:li:ts_contract:454242226,12771238020))),candidates:List((urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:822788489),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:471749602),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:321738690),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:264380410),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:79594111),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:456103694),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:703614994),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:1000008365),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:853897833),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:759058262),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:886302767),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:355893023),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:836786118),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:354506061),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:1068418612),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:500083085),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:20695580),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:870075147),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:389225849),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:1025019805),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:724108945),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:709750789),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:573883196),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:456381588),urn:li:ts_hiring_candidate:(urn:li:ts_contract:454242226,urn:li:ts_hire_identity:363934506))))"  # noqa
    )
    # main(
    #     "(facetSelections:List((type:SOURCING_CHANNEL,valuesWithSelections:List()),(type:CANDIDATE_HIRING_STATE,valuesWithSelections:List((value:urn%3Ali%3Ats_hiring_state%3A%28urn%3Ali%3Ats_contract%3A454254206%2C12771247229%29,selected:true,selected:false,required:false),(value:urn%3Ali%3Ats_hiring_state%3A%28urn%3Ali%3Ats_contract%3A454254206%2C12771251051%29,selected:true,negated:false,required:false),(value:urn%3Ali%3Ats_hiring_state%3A%28urn%3Ali%3Ats_contract%3A454254206%2C12771252348%29,selected:true,negated:false,required:false),(value:urn%3Ali%3Ats_hiring_state%3A%28urn%3Ali%3Ats_contract%3A454254206%2C12771251050%29,selected:true,negated:false,required:false)))),capSearchSortBy:HIRING_CANDIDATE_LAST_UPDATED_DATE,hiringProjects:List((text:python,entity:urn%3Ali%3Ats_hiring_project%3A%28urn%3Ali%3Ats_contract%3A454254206%2C1042246722%29)))"
    # )