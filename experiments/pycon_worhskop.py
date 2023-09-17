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




