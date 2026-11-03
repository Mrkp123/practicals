
# 1. Import package
import textkit

print(textkit.VERSION)


# 2. Import tidy through package
from textkit import tidy

print(tidy(" hello python world "))


# 3. Access slug using full module path
print(textkit.clean.slug("Data Science Lab"))


# 4. Import stats using alias
import textkit.stats as ts

print(
    ts.word_count("python is fun"),
    ts.longest_word("learn modules today")
)


# 5. Import functions from sub-package
from textkit.extra.frame import box, underline

print(box("ok"))
print(underline("Title"))
