from pyparsing import Word
import pyparsing as pp

text = pp.Word("pyconczpyconhu")
print(text.parseString("pyconcz"))
print(text.parseString("pycon"))

text = pp.Literal(",")
print(text.parseString(","))
print(text.parseString("."))

text = pp.Optional(pp.Word("pyconczpyconhu"))
print(text.parseString("We are here, pyconcz"))
print(text.parseString("pyconcz, we are here"))

text = pp.Word(pp.alphas)
print(text.parseString("We are here, pyconcz"))

text = pp.OneOrMore(pp.Word(pp.alphas))
print(text.parseString("We are here, pyconcz"))

text = pp.OneOrMore(pp.Word(pp.alphanums))
print(text.parseString("We are here in year 2023, pyconcz"))

text = pp.ZeroOrMore(pp.Word(pp.nums))
print(text.parseString("2023 is the year of pycon"))

#Define grammar
greete = pp.Word("HeyHelloHi")
comma = pp.Literal(",")
name = pp.Word(pp.alphas)
exclamation = pp.Literal("!")

# Group grammer expressions together
greeting = pp.Group(greete + pp.Optional(comma) + name + exclamation)

# Test the parser
test_str1 = "Hello, John!"
test_str2 = "Hi Emily"
test_str3 = "Hey, Sarah?"

print(greeting.parseString(test_str1))
print(greeting.parseString(test_str2))
print(greeting.parseString(test_str3))

from pyparsing import Word
import pyparsing as pp


#Define grammar
greete = pp.Word("HeyHelloHi")
comma = pp.Literal(",")
name = pp.Word(pp.alphas)
exclamation = pp.Word("!?")

# Group grammer expressions together
greeting = pp.Group(greete + pp.Optional(comma) + name + pp.Optional(exclamation))

# Test the parser
test_str1 = "Hello, John!"
test_str2 = "Hi Emily"
test_str3 = "Hey, Sarah?"

print(greeting.parseString(test_str1))
print(greeting.parseString(test_str2))
print(greeting.parseString(test_str3))

identifier = pp.Word(pp.alphas, pp.alphanums)
numeric_value = pp.Word(pp.nums+".")
combined_assigement = identifier + "=" + (identifier | numeric_value)

print(combined_assigement.parseString("pi=3.14159"))
print(combined_assigement.parseString("a = 10"))
print(combined_assigement.parseString("a2=100"))
print(combined_assigement.parseString("a=10a2"))

identifier = pp.Word(pp.alphas, pp.alphanums+"_")
numeric_value = pp.Word(pp.nums+".")
combined_assigement = identifier + "=" + (identifier | numeric_value)

print(combined_assigement.parseString("pi=3.14159"))
print(combined_assigement.parseString("a = 10"))
print(combined_assigement.parseString("a_2=100"))
print(combined_assigement.parseString("a1=10a2"))

assignment_expr = identifier.setResultsName("lhs") + "=" + (identifier | numeric_value).setResultsName("rhs")
assignment_tokens = assignment_expr.parseString("pi=3.14159")
print(assignment_tokens.lhs)
print(assignment_tokens.rhs)
print("Do you know, that " + assignment_tokens.lhs + " has value " + assignment_tokens.rhs)

word = Word(pp.alphas+"'.")
salutation = pp.OneOrMore(word)
comma = pp.Literal(",")
greetee = pp.OneOrMore(word)
endpunc = pp.oneOf("! ?")
greeting = salutation + comma + greetee + endpunc


print(greeting.parseString("Hello, Sveta?"))


salutation = pp.Group(pp.OneOrMore(word))
greetee = pp.Group(pp.OneOrMore(word))
greeting = salutation + comma + greetee + endpunc

print(greeting.parseString("Hello, Sveta?"))


comma = pp.Suppress(pp.Literal(","))

greeting = salutation + comma + greetee + endpunc

print(greeting.parseString("Hello, Sveta?"))

year = pp.Word(pp.nums, exact=4).setResultsName('year')
month = pp.Word(pp.nums, exact=2).setResultsName('month')
day = pp.Word(pp.nums, exact=2).setResultsName('day')
separator = pp.oneOf("- /")

ymd_format = year + separator + month + separator + day
dmy_format = day + separator + month + separator + year

date_grammar = ymd_format | dmy_format
result1 = date_grammar.parseString("2023-09-16")
result2 = date_grammar.parseString("16/09/2023")
                                   
print(f"Year: {result1['year']}, Month: {result1['month']}, Day: {result1['day']}")
print(f"Year: {result2['year']}, Month: {result2['month']}, Day: {result2['day']}")

date = pp.Word(pp.nums)
separator = pp.oneOf("- /")
date_grammar = pp.ZeroOrMore(date + pp.Optional(pp.Suppress(separator)))

result1 = date_grammar.parseString("2023-09-16")
result2 = date_grammar.parseString("16/09/2023")

print(result1)
print(result2)

alphaword = Word(pp.alphas)
integer = Word(pp.nums)
sexp = pp.Forward()
LPAREN = pp.Suppress("(")
RPAREN = pp.Suppress(")")
sexp << (alphaword | integer | ( LPAREN + pp.ZeroOrMore(sexp) + RPAREN))

print(sexp.parseString("( red 100 blue )"))
print(sexp.parseString("( green ( ( 1 2 ) mauve ) plaid () )"))
print(sexp.parseString("green ( ( 1 2 ) mauve ) plaid () )"))

alphaword = Word(pp.alphas)
integer = Word(pp.nums)
sexp = pp.Forward()
LPAREN = pp.Suppress("(")
RPAREN = pp.Suppress(")")
sexp << (alphaword | integer | pp.Group(LPAREN + pp.ZeroOrMore(sexp) + RPAREN))

print(sexp.parseString("( red 100 blue )"))
print(sexp.parseString("( green ( ( 1 2 ) mauve ) plaid () )"))

alphaword = Word(pp.alphas)
integer = Word(pp.nums)
sexp = pp.Forward()
LPAREN = pp.Suppress("(")
RPAREN = pp.Suppress(")")
sexp << pp.OneOrMore((alphaword | integer | pp.Group(LPAREN + pp.ZeroOrMore(sexp) + RPAREN)))

print(sexp.parseString("green ( ( 1 2 ) mauve ) plaid () )"))

real = Word(pp.nums) + '.' + Word(pp.nums)
print(real.parse_string('3.1416'))

real = pp.Combine(Word(pp.nums) + '.' + Word(pp.nums))
print(real.parse_string('3.1416'))

from pyparsing import Word, alphas, nums, Suppress, Dict

# Define what a key and a value should look like
key = Word(alphas)
value = Word(nums)

# Define a key-value pair
key_value_pair = key + Suppress(":") + value

# Use Dict to define the overall pattern
pattern = Dict(pp.OneOrMore(pp.Group(key_value_pair)))

# Parse a string
result = pattern.parseString("age: 30 height: 170 weight: 70")

# Accessing values by key
print(result)

result = pattern.parseString("age: 30 height: 170 weight: 70").as_dict()

# Accessing values by key
print(result)


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
    
import pyparsing as pp

LPAREN, RPAREN, COLON, COMMA = (
    pp.Suppress("("),
    pp.Suppress(")"),
    pp.Literal(":"),
    pp.Suppress(","),
)


def main(data: str):
    list_ = pp.Literal("List")
    base_keyword = pp.Word(pp.alphas + pp.alphas + "_")
    keyword = pp.Combine(
        base_keyword + pp.OneOrMore(COLON + (list_ | base_keyword))
    ).set_results_name("dict_key")
    keyword_with_optional_colon = keyword + pp.Optional(pp.Suppress(COLON))
    number = pp.Word(pp.nums).set_results_name("numeric_value")
    number_tuple = pp.Group(number + COMMA + number).set_results_name("numeric_tuple")
    s_expression = pp.Forward()
    s_expression << (
        keyword_with_optional_colon
        | number_tuple
        | number
        | pp.Group(LPAREN + (pp.ZeroOrMore(s_expression | pp.Suppress(COMMA))) + RPAREN)
    )
    s_expression_parsed = s_expression.parse_string(data)
    print(s_expression_parsed.as_list())  # noqa: T201


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




