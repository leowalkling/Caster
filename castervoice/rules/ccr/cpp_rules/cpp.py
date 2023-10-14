'''
Created on Sep 1, 2015

@author: synkarius
'''
from dragonfly import Choice, Mimic

from castervoice.lib.actions import Text, Key
from castervoice.rules.ccr.standard import SymbolSpecs
from castervoice.lib.const import CCRType
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.mergerule import MergeRule
from castervoice.lib.merge.state.short import R


class CPP(MergeRule):
    pronunciation = "C plus plus"

    PREFIX = "CPP"

    mapping = {
        PREFIX + SymbolSpecs.IF:
            R(Key("i, f, lparen, rparen, leftbrace, enter,up,left")),
        PREFIX + SymbolSpecs.ELSE:
            R(Key("e, l, s, e, leftbrace, enter")),
        #
        PREFIX + SymbolSpecs.SWITCH:
            R(Text("switch(){\ncase : break;\ndefault: break;") + Key("up,up,left,left")),
        PREFIX + SymbolSpecs.CASE:
            R(Text("case :") + Key("left")),
        PREFIX + SymbolSpecs.BREAK:
            R(Text("break;")),
        PREFIX + SymbolSpecs.DEFAULT:
            R(Text("default: ")),
        #
        PREFIX + SymbolSpecs.DO_LOOP:
            R(Text("do {}") + Key("left, enter:2")),
        PREFIX + SymbolSpecs.WHILE_LOOP:
            R(Text("while ()") + Key("left")),
        PREFIX + SymbolSpecs.FOR_LOOP:
            R(Text("for (std::ptrdiff_t i{0}; i < TOKEN; ++i)")),
        PREFIX + SymbolSpecs.FOR_EACH_LOOP:
            R(Text("for (const auto& TOKEN : TOKEN)")),
        #
        PREFIX + SymbolSpecs.TO_INTEGER:
            R(Text("(int)")),
        PREFIX + SymbolSpecs.TO_FLOAT:
            R(Text("(double)")),
        PREFIX + SymbolSpecs.TO_STRING:
            R(Text("std::to_string()") + Key("left")),
        #
        PREFIX + SymbolSpecs.AND:
            R(Text("&&")),
        PREFIX + SymbolSpecs.OR:
            R(Text("||")),
        PREFIX + SymbolSpecs.NOT:
            R(Text("!")),
        #
        PREFIX + SymbolSpecs.SYSOUT:
            R(Text("cout <<")),
        #
        PREFIX + SymbolSpecs.IMPORT:
            R(Text("#include")),
        #
        PREFIX + SymbolSpecs.FUNCTION:
            R(Text("TOKEN TOKEN(){}") + Key("left")),
        PREFIX + SymbolSpecs.CLASS:
            R(Text("class TOKEN{}") + Key("left")),
        #
        PREFIX + SymbolSpecs.COMMENT:
            R(Text("//")),
        PREFIX + SymbolSpecs.LONG_COMMENT:
            R(Text("/**/") + Key("left, left")),
        #
        PREFIX + SymbolSpecs.NULL:
            R(Text("null")),
        #
        PREFIX + SymbolSpecs.RETURN:
            R(Text("return")),
        #
        PREFIX + SymbolSpecs.TRUE:
            R(Text("true")),
        PREFIX + SymbolSpecs.FALSE:
            R(Text("false")),

        # C++ specific
        PREFIX + "public":
            R(Text("public ")),
        PREFIX + "private":
            R(Text("private ")),
        PREFIX + "static":
            R(Text("static ")),
        PREFIX + "final":
            R(Text("final ")),
        PREFIX + "inline":
            R(Text("inline ")),
        PREFIX + "static cast integer":
            R(Text("static_cast<int>()") + Key("left")),
        PREFIX + "static cast double":
            R(Text("static_cast<double>()") + Key("left")),
        PREFIX + "([global] scope | name)":
            R(Text("::")),
        # PREFIX + "Vic":
        #     R(Text("vector")),
        PREFIX + "tuple":
            R(Text("std::tuple")),
        PREFIX + "amp optional":
            R(Text("amp::optional")),
        PREFIX + "amp static vector":
            R(Text("amp::static_vector")),
        PREFIX + "pushback":
            R(Text("push_back")),
        PREFIX + "standard":
            R(Text("std::")),
        PREFIX + "amp":
            R(Text("amp::")),
        PREFIX + "amp PMR":
            R(Text("amp::pmr::")),
        PREFIX + "constant":
            R(Text("const")),
        PREFIX + "typename": R(Text("typename")),
        PREFIX + "auto": R(Text("auto")),
        PREFIX + "array":
            R(Mimic("brackets")),

        #http://www.learncpp.com/cpp-tutorial/67-introduction-to-pointers/
        PREFIX + "(reference to | address of)":
            R(Text("&")),
        PREFIX + "(pointer | D reference)":
            R(Text("*")),
        PREFIX + "member":
            R(Text("->")),
        PREFIX + "new new":
            R(Text("new ")),
        PREFIX + "integer":
            R(Text("int ")),
        PREFIX + "double":
            R(Text("double ")),
        PREFIX + "character":
            R(Text("char ")),
        PREFIX + "big integer":
            R(Text("Integer")),
        PREFIX + "string":
            R(Text("string ")),
        PREFIX + "ternary":
            R(Text("()?;") + (Key("left")*3)),
            
        # Customized
        PREFIX + "[<signedness>] int <nbits>": R(Text("std::%(signedness)sint%(nbits)s_t")),
        PREFIX + "PTR diff": R(Text("std::ptrdiff_t")),
        PREFIX + "deckle val":
            R(Text("std::declval")),
    }

    extras = [
        Choice("signedness", {
            "(U | you)": "u",
            "(S | signed)": "",
        }),
        Choice("nbits", {
            "(eight | 8)": "8",
            "(sixteen | 16)": "16",
            "(thirty two | 32)": "32",
            "(sixty four | 64)": "64"
        }),
    ]
    defaults = {
        "signedness": "",
    }


def get_rule():
    return CPP, RuleDetails(ccrtype=CCRType.GLOBAL)
